from django.conf import settings
from django.urls import reverse

from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter


class AccountAdapter(DefaultAccountAdapter):

    def is_open_for_signup(self, request):
        return getattr(settings, 'ACCOUNT_ALLOW_REGISTRATION', True)

    def get_email_confirmation_redirect_url(self, request):
        return reverse('users:update')

    def get_login_redirect_url(self, request):
            if request.user.name:
                if hasattr(request.user,'patient'):
                    return reverse(
                        viewname='notifications:patient_notifications'
                )
                if hasattr(request.user, 'responsible'):
                    return reverse(
                        viewname='notifications:responsible_notifications'
                    )
                if hasattr(request.user, 'healthteam'):
                    return reverse(
                        viewname='notifications:health_team_notifications'
                )
                if hasattr(request.user, 'employee'):
                    return reverse(
                        viewname='notifications:employee_notifications'
                )
                else:
                    return reverse(
                        viewname='users:detail',
                        kwargs={'username': request.user.username}
                    )
            else:
                return reverse('users:update')


class SocialAccountAdapter(DefaultSocialAccountAdapter):

    def is_open_for_signup(self, request):
        return getattr(settings, 'ACCOUNT_ALLOW_REGISTRATION', True)
