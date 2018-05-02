from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic import (DetailView, ListView, RedirectView,
                                  UpdateView, DeleteView, View)
from search_views.search import SearchListView
from search_views.filters import BaseFilter
from django.urls import reverse_lazy
from ..models import User, Patient, Employee, HealthTeam, Responsible
from ..forms.users_forms import PatientSearchForm


class PatientFilter(BaseFilter):
    search_fields = {
       'list_patient': ['id'],
    }


class UserDeleteView (LoginRequiredMixin, DeleteView):
    model = User
    # Redirect to home page
    success_url = reverse_lazy('core:home')

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        # Redirect to success_url
        return super(UserDeleteView, self).get_success_url()


class UserDetailView(UserPassesTestMixin, LoginRequiredMixin, DetailView):
    model = User
    # These next two lines tell the view to index lookups by username
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_login_url(self):
        if self.request.user.is_authenticated:
            # redirect when user tries to access other user's detail view
            login_url = reverse(
                viewname='users:detail',
                kwargs={'username': self.request.user.username}
            )
            return login_url
        else:
            login_url = reverse('account_login')
            return login_url

    def test_func(self):
        # checks if user is trying to access his own profile
        return self.request.user.username == self.kwargs.get('username')

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

        elif hasattr(user, 'healthteam'):
            context['health_team_cpf'] = user.healthteam.cpf
            context['health_team_register_number'] = \
                user.healthteam.register_number
            context['health_team_registration_state'] = \
                user.healthteam.get_registration_state_display()
            context['health_team_council_acronym'] = \
                user.healthteam.get_council_acronym_display()
            context['health_team_speciality'] = \
                user.healthteam.get_speciality_display()


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


class PatientListViewSelector(RedirectView):

    def get(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            # redirect not not authenticated to login screen
            self.url = reverse(
                viewname='account_login',
            )
            return redirect(url)

        if hasattr(request.user, 'patient'):
            # redirect user_patient to the its medical sheet view
            url = reverse(
                viewname='users:patient_medical_sheet',
                kwargs={'username': request.user.username}
            )
            return redirect(url)

        if hasattr(request.user, 'responsible'):
            url = reverse(
                viewname='users:responsible_patient_list',
            )
            return redirect(url)

        if hasattr(request.user, 'healthteam'):
            url = reverse(
                viewname='users:responsible_patient_list',
            )
            return redirect(url)


class ResponsiblePatientListView(ListView):

    # the List View will list the patients that belong to the
    # current user (specialized as a responsible), only responsibles will
    # access this view
    model = Patient
    template_name = 'users/responsible_patient_list.html'
    paginate_by = 10

    def get(self, request, *args, **kwargs):

        if not hasattr(request.user, 'responsible'):
            # redirect user_patient to the its medical sheet view
            url = reverse(
                viewname='account_login',
            )
            return redirect(url)

        return super().get(request, *args, **kwargs)

    def get_queryset(self, *args, **kwargs):

        user = self.request.user
        return super().get_queryset(*args, **kwargs).filter(
            responsible=user.responsible
        )


class HealthTeamPatientListView(SearchListView):

    # the List View will list patients and will allow
    # for the current user (specialized as a healthteam),
    # to search them

    model = Patient
    template_name = 'users/healthteam_patient_list.html'
    form_class = PatientSearchForm
    filter_class = PatientFilter
    paginate_by = 20

    def get(self, request, *args, **kwargs):

        if not hasattr(request.user, 'healthteam'):
            # redirect user_patient to the its medical sheet view
            url = reverse(
                viewname='account_login',
            )
            return redirect(url)

        return super().get(request, *args, **kwargs)


class PatientDetailView(DetailView):
    model = Patient
