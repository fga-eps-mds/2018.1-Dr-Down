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
            return reverse(
                        viewname='users:detail', 
                        kwargs={'username': request.user.username}
            )
        else:
            return reverse('users:update')


class SocialAccountAdapter(DefaultSocialAccountAdapter):

    def is_open_for_signup(self, request):
        return getattr(settings, 'ACCOUNT_ALLOW_REGISTRATION', True)
