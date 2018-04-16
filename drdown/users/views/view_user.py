from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views.generic import (DetailView, ListView, RedirectView,
                                  UpdateView, DeleteView)
from django.urls import reverse_lazy

from ..models import User


class UserDeleteView (LoginRequiredMixin, DeleteView):

    """
    Delete the user account
    """

    model = User

    # Redirect to home page
    success_url = reverse_lazy('home')

    def get_object(self):
        """
        Search a ID or slug from url and return a object from model.
        In this case return the current user logged from model.
        """

        return self.request.user

    def get_success_url(self):

        # Redirect to success_url
        return super(UserDeleteView, self).get_success_url()


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super(UserDetailView, self).get_context_data(**kwargs)

        self.prepare_context_data(user, context)

        return context

    def prepare_context_data(self, user, context):
        if hasattr(user, 'patient'):

            context['patient_ses'] = user.patient.ses
            context['patient_priority'] = (user.patient.get_priority_display())
            context['patient_mother_name'] = user.patient.mother_name
            context['patient_father_name'] = user.patient.father_name
            context['patient_ethnicity'] = \
                (user.patient.get_ethnicity_display())
            context['patient_sus_number'] = user.patient.sus_number
            context['patient_civil_registry_of_birth'] = \
                user.patient.civil_registry_of_birth
            context['patient_declaration_of_live_birth'] = \
                user.patient.declaration_of_live_birth

        elif hasattr(user, 'responsible'):

            context['responsible_cpf'] = user.responsible.cpf
            patients = list(user.responsible.patient_set.all())
            context['responsible_patient'] = patients

        elif hasattr(user, 'employee'):

            context['employee_cpf'] = user.employee.cpf
            context['employee_department'] = (
                        user.employee.get_departament_display()
                        )

        elif hasattr(user, 'health_team'):
            context['health_team_cpf'] = user.health_team.cpf
            context['health_team_register_number'] = user.health_team.register_number
            context['health_team_registration_state'] = user.health_team.get_registration_state_display()
            context['health_team_council_acronym'] = user.health_team.get_council_acronym_display()
            context['health_team_speciality'] = user.health_team.get_speciality_display()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})


class UserUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', 'gender', 'telephone', 'birthday', 'photo']

    # we already imported User in the view code above, remember?
    model = User

    # send the user back to their own page after a successful update
    def get_success_url(self):
        return reverse('users:detail',
                       kwargs={'username': self.request.user.username})

    def get_object(self):
        # Only get the User record for the user making the request
        return User.objects.get(username=self.request.user.username)


@method_decorator(user_passes_test(lambda u: u.is_superuser,
                  login_url='users:redirect'), name='dispatch')
class UserListView(LoginRequiredMixin, ListView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'
