from ..models.model_post import Post
from ..models.model_category import Category
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from datetime import datetime


class PostListView(ListView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        context['post_category'] = Category.objects.get(pk=pk)
        return context

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        queryset = Post.objects.filter(category=Category.objects.get(pk=pk))
        return queryset


class PostCreateView(CreateView):
    model = Post
    template_name = 'forum/form_post.html'
    fields = ['title', 'message']
    success_url = reverse_lazy('forum:list_categories')

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
        form.instance.updated_at = datetime.now()
        form.save()

        return super(PostUpdateView, self).form_valid(form)
