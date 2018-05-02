from django.shortcuts import get_object_or_404, render, redirect
from django.http import (
    HttpResponseRedirect,
    HttpResponse,
    HttpResponseForbidden,
    HttpResponseServerError,
    HttpResponsePermanentRedirect
)
from django.urls import reverse

from django.utils.translation import ugettext_lazy as _

from drdown.careline.models import (
    Checklist,
    Procedure,
    CheckItem
)
from django.views.generic import (
    DetailView,
    ListView,
    TemplateView,
    RedirectView
)
from drdown.users.models import User, Patient


class ChecklistRedirectView(RedirectView):

    # redirect this page to user list of
    # medical follow-up sheet page
    url = 'users:patient_list'
    permanent = True

    def get(self, request, *args, **kwargs):
        return HttpResponsePermanentRedirect(reverse(self.url), request)


class ChecklistDetailView(DetailView):
    model = Checklist
    template_name = 'careline/checklist_detail.html'

    def get(self, request, *args, **kwargs):

        current_user = request.user
        target_user = get_object_or_404(User, username=kwargs.get('username'))

        if (
            not hasattr(target_user, 'patient') or
            not self.has_permission(current_user=current_user,
                                    target_user=target_user)
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

    @staticmethod
    def has_permission(current_user, target_user):

        allowed = False

        # here using '==' is intended
        if current_user == target_user:
            # if we are the patient that the page is trying to access
            allowed = True

        elif hasattr(current_user, 'responsible'):
            # if we are someone else, we need to check permissions
            # for instance, if the current user is a responsible
            # of the target user
            for patient in current_user.responsible.patient_set.all():
                if patient.user == target_user:
                    allowed = True

        return allowed

    def prepare_context_data(self, user, context):

        if hasattr(user, 'patient') and hasattr(user.patient, 'checklist'):
            context['checklist'] = user.patient.checklist


class ChecklistUpdateView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):

        return reverse(
            viewname='careline:checklist_list',
        )

    @staticmethod
    def has_permission(current_user, target_user):

        allowed_on_view = ChecklistDetailView.has_permission(
                current_user=current_user,
                target_user=target_user
            )

        return (allowed_on_view and current_user.age() >= 13)

    def post(self, request, *args, **kwargs):

        target_user = User.objects.get(
            username=request.POST.get('username')
        )

        if(
            self.has_permission(
                current_user=request.user,
                target_user=target_user
            )
        ):
            message = self.process_change(
                user=target_user,
                checklist_id=request.POST.get('checklist_id'),
                procedure_id=request.POST.get('procedure_id'),
                value=request.POST.get('value')
            )
        else:
            message = _("Error: You cannot change data on this form. "
                        "You need to be at least 13 years old.")
            return HttpResponseForbidden(message)

        return HttpResponse(message)

    def process_change(self, user, checklist_id, procedure_id, value):

        procedure = user.patient.checklist.procedure_set.get(id=procedure_id)
        check_item = procedure.checkitem_set.get(id=checklist_id)

        check_item.check = value
        check_item.save()
        check_item.refresh_from_db()

        return _("Success! Your changes were saved.")
