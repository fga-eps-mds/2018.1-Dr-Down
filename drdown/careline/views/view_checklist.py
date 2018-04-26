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

    def get(self, request, *args, **kwargs):

        current_user = request.user
        target_user = User.objects.get(username=kwargs.get('username'))

        if (
            not hasattr(target_user, 'patient') or
            not self.has_permission(current_user=current_user, target_user=target_user)
        ):
            url = reverse(
                viewname='careline:checklist_list',
            )
            return redirect(url)

        self.object = self.get_object(*args, **kwargs)
        context = self.get_context_data(object=self.object)

        return self.render_to_response(context)

    def get_object(self, queryset=None, *args, **kwargs):
        target = User.objects.get(username=kwargs.get('username'))

        return target.patient.checklist

    def get_context_data(self, **kwargs):

        context = super(ChecklistDetailView, self).get_context_data(**kwargs)

        target_user = User.objects.get(username=self.kwargs.get('username'))

        self.prepare_context_data(target_user, context)

        return context

    def has_permission(self, current_user, target_user):

        allowed = False

        # here using '==' is intended
        if current_user == target_user:
            # if we are the patient that the page is trying to access
            allowed = True

        elif hasattr(current_user, 'responsible'):
            # if we are someone else, we need to check permissions
            # for instance, if the current user is a responsible of the target user
            for patient in current_user.responsible.patient_set.all():
                if patient.user == target_user:
                    allowed = True

        return allowed

    def prepare_context_data(self, user, context):

        if hasattr(user, 'patient') and hasattr(user.patient, 'checklist'):
            context['checklist'] = user.patient.checklist
