from django.conf.urls import url
from .views.view_category import CategoryListView
from .views.view_post import PostListView
from .views.view_post import PostCreateView

app_name = 'forum'
urlpatterns = [
    url(
        regex=r'^$',
        view=CategoryListView.as_view(),
        name='list_categories'
    ),
    url(
        regex=r'^categories/(?P<slug>[-\w]+)-(?P<pk>\d+)/$',
        view=PostListView.as_view(),
        name='list_posts'
    ),
    url(
        regex=r'^categories/(?P<slug>[-\w]+)-(?P<pk>\d+)/new/$',
        view=PostCreateView.as_view(),
        name='create_post'
    ),
]
