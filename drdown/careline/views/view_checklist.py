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

        user = self.request.user

        queryset = None

        if hasattr(user, "responsible"):
            queryset = Patient.objects.filter(responsible=user.responsible)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user
        patients = Patient.objects.filter(responsible=user.responsible)

        context['patient_list'] = patients

        return context


class ChecklistDetailView(DetailView):
    model = Checklist
    template_name = 'careline/checklist_detail.html'

    def get_object(self, queryset=None):
        # Only get the User record for the user making the request
        user = User.objects.get(username=self.request.user.username)

        if hasattr(user, "patient"):
            return user.patient.checklist

    def get_context_data(self, **kwargs):
        current_user = self.request.user
        context = super(ChecklistDetailView, self).get_context_data(**kwargs)

        target_user = User.objects.get(username=self.kwargs.get('username'))

        # if we are the patient that the page is trying to access
        if hasattr(current_user, 'patient'):
            self.prepare_context_data(current_user, context)

        # if we are someone else, we need to check permissions
        # for instance, if the current user is a responsible of the target user
        if current_user.username is not current_user.username:
            if self.has_permission(current_user, target_user):
        self.prepare_context_data(target_user, context)

        return context

    def has_permission(self, current_user, target_user):

        # check if target_user is a patient of responsible
        if hasattr(current_user, 'responsible'):
           for patient in current_user.responsible.patient_set:
               if patient.user.username is target_user.username:
                   return True

        return False

    def prepare_context_data(self, user, context):

        if hasattr(user, 'patient') and hasattr(user.patient, 'checklist'):
            context['checklist'] = user.patient.checklist
