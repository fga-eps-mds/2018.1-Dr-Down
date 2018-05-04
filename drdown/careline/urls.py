from django.conf.urls import url

from .views import (
    ChecklistDetailView,
    ChecklistRedirectView,
    ChecklistUpdateView
)

app_name = 'careline'
urlpatterns = [
    url(
        regex=r'^$',
        view=ChecklistRedirectView.as_view(),
        name='checklist_list'
    ),
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=ChecklistDetailView.as_view(),
        name='checklist_detail'
    ),
    url(
        regex=r'^view/update$',
        view=ChecklistUpdateView.as_view(),
        name='checklist_update'
    ),
]
