from django.shortcuts import redirect, reverse

from drdown.careline.models import (
    Checklist,
    Procedure,
    CheckItem
)
from django.views.generic import DetailView, ListView

from drdown.users.models import User, Patient


class ChecklistListView(ListView):

    # the List View for Checklists will list the patients that belong to the
    # current user (specialized as a responsible), only responsibles will
    # access this view
    model = Checklist
    template_name = 'careline/checklist_list.html'

    def get(self, request, *args, **kwargs):

        if hasattr(request.user, 'patient'):
            # redirect user_patient to the checklist detail view
            url = reverse(
                viewname='careline:checklist_detail',
                kwargs={'username': request.user.username}
            )
            return redirect(url)

        if not hasattr(request.user, 'responsible'):
            url = reverse(
                viewname='users:detail',
                kwargs={'username': request.user.username}
            )
            return redirect(url)

        return super().get(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):

        user = User.objects.get(username=self.request.user.username)

        if hasattr(user, "responsible"):
            return Patient.objects.filter(responsible=user.responsible)
        else:
            return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        patients = Patient.objects.filter(responsible=user.responsible)

        context['patient_list'] = patients

        return context


    def prepare_context_data(self, user, context):
        pass


class ChecklistDetailView(DetailView):
    model = Checklist
    template_name = 'careline/checklist_detail.html'

    def get_object(self, queryset=None):
        # Only get the User record for the user making the request
        user = User.objects.get(username=self.request.user.username)

        if hasattr(user, "patient"):
            return user.patient.checklist

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(ChecklistDetailView, self).get_context_data(**kwargs)

        self.prepare_context_data(user, context)

        return context

    def prepare_context_data(self, user, context):
        pass
