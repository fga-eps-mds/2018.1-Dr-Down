from ..models.model_post import Post
from ..models.model_category import Category
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.utils.text import slugify
from datetime import datetime


class PostListView(ListView):
    model = Post
    slug_field = 'title'
    slug_url_kwarg = 'title'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['category_pk'] = self.kwargs.get('pk')
        context['category_slug'] = self.kwargs.get('slug')
        return context

    def get_queryset(self):
        queryset = Post.objects.filter(category=Category.objects.get(pk=self.kwargs.get('pk')))
        return queryset


class PostCreateView(CreateView):
    model = Post
    template_name = 'forum/form_post.html'
    fields = ['title', 'message']
    success_url = reverse_lazy('forum:list_categories')

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context['category_pk'] = self.kwargs.get('pk')
        context['category_slug'] = self.kwargs.get('slug')
        return context

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


class PostDeleteView (DeleteView):
    model = Post
    success_url = reverse_lazy('forum:list_categories')

    def get_object(self):
        post = Post.objects.get(
            pk=self.kwargs.get('post_pk')
        )
        return post


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'forum/form_post.html'
    fields = ['message']
    success_url = reverse_lazy('forum:list_categories')

    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        context['category_pk'] = self.kwargs.get('pk')
        context['category_slug'] = self.kwargs.get('slug')
        return context

    def get_object(self):
        post = Post.objects.get(
            pk=self.kwargs.get('post_pk')
        )
        return post

    def form_valid(self, form):

        # Get updated_at datetime
        form.instance.updated_at = datetime.now()
        form.save()

        # Change slug to new title
        form.instance.slug = slugify(
            str(form.instance.id) +
            "-" +
            form.instance.title
        )
        form.save()
        return super(PostUpdateView, self).form_valid(form)





