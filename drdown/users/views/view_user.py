from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from ..models import User


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(UserDetailView, self).get_context_data(**kwargs)
        if hasattr(user, 'patient'):
            context['patient_ses'] = user.patient.ses
            context['patient_priority'] = user.patient.priority
            context['patient_mother_name'] = user.patient.mother_name
            context['patient_father_name'] = user.patient.father_name
            context['patient_ethnicity'] = user.patient.ethnicity
            context['patient_sus_number'] = user.patient.sus_number
            context['patient_civil_registry_of_birth'] = user.patient.civil_registry_of_birth
            context['patient_declaration_of_live_birth'] = user.patient.declaration_of_live_birth
        elif hasattr(user, 'responsible'):
            context['responsible_cpf'] = user.responsible.cpf
            context['responsible_patient'] = user.responsible.patient
        return context


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', ]

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'
