from ..models.model_post import Post
from ..models.model_category import Category
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.utils.text import slugify


class PostListView(ListView):
    model = Post
    slug_field = 'title'
    slug_url_kwarg = 'title'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['category_pk'] = self.kwargs.get('pk')
        context['category_slug'] = self.kwargs.get('slug')
        return context


class PostCreateView(CreateView):
    model = Post
    template_name = 'forum/form_post.html'
    fields = ['title', 'message']
    success_url = reverse_lazy('forum:list_categories')

    def form_valid(self, form):

        # Get category that post belongs to
        form.instance.category = Category.objects.get(pk=self.kwargs.get('pk'))
        form.instance.created_by = self.request.user
        form.save()

        # Save slug with post title
        form.instance.slug = slugify(
            str(form.instance.id) +
            "-" +
            form.instance.title
        )
        form.save()

        return super(PostCreateView, self).form_valid(form)

class PostDeleteView ( DeleteView):


    model = Post

    success_url = reverse_lazy('forum:list_categories')


    def get_success_url(self):

        return super(PostDeleteView, self).get_success_url()




