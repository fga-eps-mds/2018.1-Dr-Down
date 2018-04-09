from ..models.model_post import Post
from django.views.generic import ListView


class PostListView(ListView):
    model = Post
    slug_field = 'title'
    slug_url_kwarg = 'title'


