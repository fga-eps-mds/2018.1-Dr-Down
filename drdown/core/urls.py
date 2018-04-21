from django.conf.urls import url
from django.views.generic import TemplateView


app_name = 'core'
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='core/home.html'), name='home'),
    url(r'^info/$', TemplateView.as_view(template_name='core/info.html'), name='about'),
]
