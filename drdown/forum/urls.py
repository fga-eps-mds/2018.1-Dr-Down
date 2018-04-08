from django.conf.urls import url
from . import views

app_name = 'forum'
urlpatterns = [
    url(
        regex=r'^$',
        view=views.CategoryListView.as_view(),
        name='list_category'
    ),
]
