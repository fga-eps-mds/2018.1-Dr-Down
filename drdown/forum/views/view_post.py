from ..models.model_post import Post
from ..models.model_category import Category
from .view_base import BaseViewTemplate
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.utils import timezone
from drdown.forum.form.forum_forms import PostForm


class PostListView(BaseViewTemplate, ListView):
    model = Post
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['post_category'] = Category.objects.get(pk=pk)
        return context

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        queryset = Post.objects.filter(
            category=Category.objects.get(pk=pk)
        ).order_by('-created_at')
        return queryset


class PostCreateView(BaseViewTemplate, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'forum/form_post.html'

    def get_success_url(self, **kwargs):
        success_create_url = reverse_lazy(
            viewname='forum:list_posts',
            kwargs={
                'slug': self.kwargs.get('slug'),
                'pk': self.kwargs.get('pk'),
            }
        )
        return success_create_url

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['post_category'] = Category.objects.get(pk=pk)
        return context

    def form_valid(self, form):
        # Get category that post belongs to
        form.instance.category = Category.objects.get(pk=self.kwargs.get('pk'))
        form.instance.created_by = self.request.user
        form.save()

        return super(PostCreateView, self).form_valid(form)


class PostDeleteView (BaseViewTemplate, DeleteView):
    model = Post

    def get_success_url(self, **kwargs):
        success_delete_url = reverse_lazy(
            viewname='forum:list_posts',
            kwargs={
                'pk': self.kwargs.get('pk'),
                'slug': self.kwargs.get('slug'),
            }
        )
        return success_delete_url

    def get_object(self):
        post = Post.objects.get(
            pk=self.kwargs.get('post_pk')
        )
        return post


class PostUpdateView(BaseViewTemplate, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'forum/form_post.html'

    def get_success_url(self, **kwargs):
        success_update_url = reverse_lazy(
            viewname='forum:list_commentary',
            kwargs={
                'pk': self.kwargs.get('pk'),
                'post_pk': self.kwargs.get('post_pk'),
                'slug': self.kwargs.get('slug'),
            }
        )
        return success_update_url

    def get_context_data(self, **kwargs):
        context = super(PostUpdateView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['post_category'] = Category.objects.get(pk=pk)
        return context

    def get_object(self):
        post = Post.objects.get(
            pk=self.kwargs.get('post_pk')
        )
        return post

    def form_valid(self, form):
        # Get updated_at datetime
        form.instance.updated_at = timezone.now()
        form.save()

        return super(PostUpdateView, self).form_valid(form)
