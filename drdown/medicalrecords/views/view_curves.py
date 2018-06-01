from ..models.model_curves import Curves
from drdown.users.models.model_patient import Patient
from django.views.generic import CreateView,  UpdateView, View
from ..forms.curves_form import CurvesForm
from ..views.views_base import BaseViewUrl, BaseViewPermissions
from django.shortcuts import get_object_or_404, redirect
from django.http import (
    HttpResponse,
    HttpResponseForbidden,
    JsonResponse,
)
from django.urls import reverse, reverse_lazy

from urllib import parse, request as urlrequest
import json


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


class CurvesUpdateView(
    BaseViewPermissions, BaseViewUrl, UpdateView
):
    model = Curves
    form_class = CurvesForm
    template_name = 'medicalrecords/medicalrecord_curves_form.html'


class CurveDataParser(BaseViewPermissions, View):

    api_port = ":8000"
    patient = None
    data_type = None
    api_url = None
    drdown_data = None
    api_data = None

    def get(self, request, *args, **kwargs):

        self.patient = Patient.objects.filter(
            user__username=request.GET.get('username')
        ).first()

        self.data_type = request.GET.get('data_type')

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

        if gender == "M" or "Male":
            return "male"
        else:
            return "female"

    def api_time_frame(self):

        # TODO
        return "months"

    def get_api_directory(self):

        # API directory map:

        # api/growth-curve/height/
        # api/growth-curve/weight/
        # [male-months, male-years, female-months, female-years, result]

        # api/growth-curve/imc/
        # api/growth-curve/perimeter/
        # [male, female, result]

        api_dir = "api/growth-curve/" + self.api_data_type() + "/" + self.api_gender()

        if self.api_data_type() not in ["imc", "perimeter"]:
            api_dir += "-" + self.api_time_frame()

        return api_dir

    def get_api_data(self):

        # Ideally, in place of the constant, one would use self.api_url
        # but its not working right now
        API_URL = "drdown-homolog.ml:8000"

        url = "http://" + API_URL + "/" + self.get_api_directory()
        print("DEBUG >>> URL " + url)

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
            graph_list = graphic[data[0] + 1]

            # the last element is the value
            graph_list[-1] = data[1]

        return self.api_data

    def select_data(self):

        selected_curves = []

        if self.api_time_frame() == 'months':

            # if we are asking for months, the API limit is 36
            selected_curves = list(
                filter(lambda x: x[0] <= 36, self.drdown_data)
            )

        elif self.api_time_frame() == 'years':

            # get data with months bigger than 36
            year_curves = list(filter(lambda x: x[0] > 36, self.drdown_data))

            # API years go from 3 to 18
            for i in range(3, 18):
                # this line filter all curve points that belongs to a year
                # ex: month 36 to month 48, then gets the last one of those
                # this behaviour was defined bt management (instead os a mean)
                selected_curves += list(
                    filter(
                        lambda x: (i * 12 <= x[0] < (i + 1) * 12), year_curves
                    )
                )[-1]

        # handy debug line, for the poor guy who will be doing maintenance
        # here in the future:

        # print("DEBUG >>>" + self.api_time_frame() + " " + 
        # self.get_api_directory() + " " + str(selected_curves))

        return selected_curves
