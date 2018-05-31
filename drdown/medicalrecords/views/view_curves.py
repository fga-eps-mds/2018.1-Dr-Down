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

from urllib import parse, request
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

            curve_data = (curve.age, getattr(curve, attr))
            data.append(curve_data)

        return data

    def get_drdown_data(self):

        curves = self.get_curves(self.patient)

        return self.get_curve_data(curves, self.data_type)

    def get_api_url(self, request):

        url = parse.urlparse(request.build_absolute_uri())
        return str(url.netloc) + self.api_port

    def api_data_type(self):
        if self.data_type == "bmi":
            return "imc/"
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
        # api/growth-curve/height/
        # api/growth-curve/weight/
        # api/growth-curve/perimeter/
        # api/growth-curve/imc/
        # [male-months, male-years, female-months, female-years, result]

        return (
            "api/growth-curve/" + self.api_data_type() + "/" +
            self.api_gender() + "-" + self.api_time_frame()
        )

    def get_api_data(self):

        url = "http://" + self.api_url + "/" + self.get_api_directory()

        req = request.Request(url=url,)

        opener = request.build_opener()
        f = opener.open(req)

        json_obj = json.loads(f.read())

        return json_obj

    def combine_data(self):

        graphic = self.api_data['graphic']

        # data_tuple: 0 is age, 1 is value

        for data_tuple in self.drdown_data:
            list = graphic[data_tuple[0] + 1]
            list[-1] = data_tuple[1]

        return self.api_data
