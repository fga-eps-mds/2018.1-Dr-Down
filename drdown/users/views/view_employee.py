from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView

from ..models import Employee


class EmployeeDetailView(DetailView):
    model = Employee
    template_name = 'employee_detail.html'
