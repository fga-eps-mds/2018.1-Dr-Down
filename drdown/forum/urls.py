from django.conf.urls import url
from .views import view_category
from .views import view_commentary
from .views import view_post


app_name = 'forum'
urlpatterns = [
    url(
        regex=r'^$',
        view=view_category.CategoryListView.as_view(),
        name='list_categories'
    ),
    url(
        regex=r'^categories/(?P<slug>[-\w]+)-(?P<pk>\d+)/$',
        view=view_post.PostListView.as_view(),
        name='list_posts'
    ),
    url(
        regex=r'^categories/(?P<slug>[-\w]+)-(?P<pk>\d+)/new/$',
        view=view_post.PostCreateView.as_view(),
        name='create_post'
    ),
    url(
        regex=r'^categories/(?P<slug>[-\w]+)-(?P<pk>\d+)/posts/(?P<post_pk>\d+)/delete/$',
        view=view_post.PostDeleteView.as_view(),
        name='delete_post'
    ),
    url(
        regex=r'^categories/(?P<slug>[-\w]+)-(?P<pk>\d+)/posts/(?P<post_pk>\d+)/edit/$',
        view=view_post.PostUpdateView.as_view(),
        name='update_post'
    ),
    url(
        regex=r'^categories/(?P<slug>[-\w]+)-(?P<pk>\d+)/posts/(?P<commentary_pk>\d+)/$',
        view=view_commentary.CommentaryListView.as_view(),
        name='list_commentary'
    ),
    url(
        regex=r'^categories/(?P<slug>[-\w]+)-(?P<pk>\d+)/posts/(?P<post_pk>\d+)/new/$',
        view=view_commentary.CommentaryCreateView.as_view(),
        name='create_commentary'
    ),
    url(
        regex=r'^categories/(?P<slug>[-\w]+)-(?P<pk>\d+)/posts/(?P<commentary_pk>\d+)/delete/$',
        view=view_commentary.CommentaryDeleteView.as_view(),
        name='delete_commentary'
    ),
]
