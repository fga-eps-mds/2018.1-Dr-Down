from django.contrib import messages
from django.db import IntegrityError
from django.utils.translation import ugettext_lazy as _
from ..models.model_curves import Curves
from drdown.users.models.model_patient import Patient
from django.views.generic import CreateView,  UpdateView, View
from ..forms.curves_form import CurvesForm
from ..views.views_base import (
    BaseViewUrl,
    BaseViewPermissions,
    BaseViewPermissionPatientResponsible
)
from django.shortcuts import get_object_or_404, redirect, render
from django.http import (
    HttpResponse,
    HttpResponseForbidden,
    JsonResponse,
)
from django.urls import reverse, reverse_lazy
from urllib import parse, request as urlrequest
import json
from math import floor


class FormValid():

    def form_valid(self, form):

        form.instance.patient = Patient.objects.get(
            user__username=self.kwargs.get('username')
        )

        form.save()

        return super().form_valid(form)


class CurvesCreateView(
    FormValid, BaseViewPermissions, BaseViewUrl, CreateView
):

    model = Curves
    form_class = CurvesForm
    template_name = 'medicalrecords/medicalrecord_curves_form.html'

    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except IntegrityError:
            messages.add_message(request, messages.ERROR,
                                 _('The patient already has a curve at this '
                                   'age. If wanted, just change its data.'))
            return render(request, template_name=self.template_name,
                          context=self.get_context_data())


class CurvesUpdateView(
    BaseViewPermissions, BaseViewUrl, UpdateView
):
    model = Curves
    form_class = CurvesForm
    template_name = 'medicalrecords/medicalrecord_curves_form.html'


class CurveDataParser(BaseViewPermissionPatientResponsible, View):

    api_port = ":8000"
    patient = None
    data_type = None
    api_url = None
    drdown_data = None
    api_data = None
    time_frame = None

    DATA_TYPE_TRANSLATIONS = {
        'bmi': _("BMI"),
        'weight': _("Weight"),
        'height': _("Height"),
        'cephalic_perimeter': _("Cephalic Perimeter"),
        'months': _("Age (in months)"),
        'years': _("Age (in years)"),
    }

    DATA_AGE_TRANSLATIONS = {
        'months': _(" (in months)"),
        'years': _(" (in years)"),
    }

    def get(self, request, *args, **kwargs):

        self.patient = Patient.objects.filter(
            user__username=request.GET.get('username')
        ).first()

        self.data_type = request.GET.get('data_type')

        self.time_frame = request.GET.get('time_frame')

        self.api_url = self.get_api_url(request)

        self.drdown_data = self.get_drdown_data()

        self.api_data = self.get_api_data()

        return JsonResponse({'data': self.combine_data()})

    @staticmethod
    def get_curves(patient):
        return Curves.objects.filter(patient=patient)

    @staticmethod
    def get_curve_data(curves, attr):

        data = []

        for curve in curves:

            # tuple, 0 == age, 1 == value
            curve_data = (curve.age, getattr(curve, attr))
            data.append(curve_data)

        return data

    def get_drdown_data(self):

        curves = self.get_curves(self.patient)

        return self.get_curve_data(curves, self.data_type)

    def get_api_url(self, request):

        # get the current addres and add service port
        url = parse.urlparse(request.build_absolute_uri())
        return str(url.netloc) + self.api_port

    def api_data_type(self):

        if self.data_type == "bmi":
            return "imc"
        elif self.data_type == "cephalic_perimeter":
            return "perimeter"
        else:
            return self.data_type

    def api_gender(self):

        gender = self.patient.user.gender

        if gender in ["M", "Male"]:
            return "male"
        else:
            return "female"

    def api_time_frame(self):

        if self.data_type == "bmi":
            return "years"
        elif self.data_type == "cephalic_perimeter":
            return "months"

        return self.time_frame

    def get_api_directory(self):

        # API directory map:

        # api/growth-curve/height/
        # api/growth-curve/weight/
        # [male-months, male-years, female-months, female-years, result]

        # api/growth-curve/imc/
        # api/growth-curve/perimeter/
        # [male, female, result]

        api_dir = (
            "api/growth-curve/" + self.api_data_type() +
            "/" + self.api_gender()
        )

        if self.api_data_type() not in ["imc", "perimeter"]:
            api_dir += "-" + self.api_time_frame()

        return api_dir

    def get_api_data(self):

        # Ideally, in place of the constant, one would use self.api_url
        # but its not working right now
        API_URL = "drdown-homolog.ml:8000"

        url = "http://" + API_URL + "/" + self.get_api_directory()
        # print("DEBUG >>> URL " + url)

        # create a request and parse response as JSON
        req = urlrequest.Request(url=url,)

        opener = urlrequest.build_opener()
        f = opener.open(req)

        json_obj = json.loads(f.read())

        return json_obj

    def combine_data(self):

        graphic = self.api_data['graphic']

        # data is a tuple with 0 == patient age, 1 == value

        for data in self.select_data():

            # the index is age + 1, because the first line
            # in the 'graphic' returned by the api is a Header line
            # so it saves no values

            age = data[0]

            index = age if self.api_time_frame() == 'months' else floor(age/12)

            if self.api_time_frame() == 'months':
                index += 1
            elif self.data_type in ['height', 'weight']:
                index -= 2
            else:
                index -= 1

            graph_list = graphic[index]

            # the last element is the value
            graph_list[-1] = data[1]

        headers = graphic[0]
        headers[0] = self.DATA_TYPE_TRANSLATIONS[self.api_time_frame()]
        headers[-1] = self.DATA_TYPE_TRANSLATIONS[self.data_type]

        return self.api_data

    def select_data(self):

        selected_curves = []

        if self.api_time_frame() == 'months':

            max_month = 24 if self.data_type == "cephalic_perimeter" else 36

            # if we are asking for months, the API limit is 36
            selected_curves = list(
                filter(lambda x: x[0] <= max_month, self.drdown_data)
            )

        elif self.api_time_frame() == 'years':

            MIN_YEAR = 2 if self.data_type == 'bmi' else 3
            MAX_YEAR = 18

            # get data with months bigger than MIN_YEAR
            year_curves = list(
                filter(lambda x: x[0] >= MIN_YEAR * 12, self.drdown_data)
            )

            # API years go from 3 to 18
            for i in range(MIN_YEAR, MAX_YEAR):
                # this line filter all curve points that belongs to a year
                # ex: month 36 to month 48, then gets the last one of those
                # this behaviour was defined bt management (instead os a mean)

                specific_year_curves = [
                    x for x in year_curves
                    if (i * 12 <= x[0] < (i + 1) * 12)
                ]

                selected_curves += specific_year_curves

        # handy debug line, for the poor guy who will be doing maintenance
        # here in the future:

        # print("DEBUG >>>" + self.api_time_frame() + " " +
        # self.get_api_directory() + " " + str(selected_curves))

        return selected_curves
