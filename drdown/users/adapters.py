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

        if not request.user.name:
            # redirect to update profile
            return reverse('users:update')

        REDIRECTS = {
            'patient': 'notifications:patient_notifications',
            'responsible': 'notifications:responsible_notifications',
            'employee': 'notifications:employee_notifications',
            'healthteam': 'notifications:health_team_notifications',
        }

        for user_type in REDIRECTS:
            if hasattr(request.user, user_type):
                return reverse(
                    viewname=REDIRECTS[user_type]
                )

        return reverse(
                    viewname='users:detail',
                    kwargs={'username': request.user.username}
                )


class SocialAccountAdapter(DefaultSocialAccountAdapter):

    def is_open_for_signup(self, request):
        return getattr(settings, 'ACCOUNT_ALLOW_REGISTRATION', True)
