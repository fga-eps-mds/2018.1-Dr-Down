from django.conf.urls import url
from .views.view_category import CategoryListView
from .views.view_post import PostListView
from .views.view_post import PostCreateView
from .views.view_post import PostDeleteView
from .views.view_post import PostUpdateView
from .views.view_commentary import CommentaryListView
from .views.view_commentary import CommentaryCreateView
from .views.view_commentary import CommentaryDeleteView


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
    url(
        regex=r'^categories/(?P<slug>[-\w]+)-(?P<pk>\d+)/posts/(?P<post_pk>\d+)/delete/$',
        view=PostDeleteView.as_view(),
        name='delete_post'
    ),
    url(
        regex=r'^categories/(?P<slug>[-\w]+)-(?P<pk>\d+)/posts/(?P<post_pk>\d+)/edit/$',
        view=PostUpdateView.as_view(),
        name='update_post'
    ),
    url(
        regex=r'^categories/(?P<slug>[-\w]+)-(?P<pk>\d+)/posts/(?P<commentary_pk>\d+)/$',
        view=CommentaryListView.as_view(),
        name='list_commentary'
    ),
    url(
        regex=r'^categories/(?P<slug>[-\w]+)-(?P<pk>\d+)/posts/(?P<post_pk>\d+)/new/$',
        view=CommentaryCreateView.as_view(),
        name='create_commentary'
    ),
    url(
        regex=r'^categories/(?P<slug>[-\w]+)-(?P<pk>\d+)/posts/(?P<commentary_pk>\d+)/delete/$',
        view=CommentaryDeleteView.as_view(),
        name='delete_commentary'
    ),
]
