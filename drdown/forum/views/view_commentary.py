from ..models.model_commentary import Commentary
from ..models.model_post import Post
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.utils.text import slugify
from datetime import datetime


class CommentaryListView(ListView):
    model = Commentary

    def get_context_data(self, **kwargs):
        context = super(CommentaryListView, self).get_context_data(**kwargs)
        context['category_pk'] = self.kwargs.get('pk')
        context['category_slug'] = self.kwargs.get('slug')
        context['post_pk'] = self.kwargs.get('post_pk')
        context['post'] = Post.objects.get(pk=self.kwargs.get('post_pk'))
        return context

    def get_queryset(self):
        queryset = Commentary.objects.filter(post=Post.objects.get(pk=self.kwargs.get('post_pk')))
        return queryset


class CommentaryCreateView(CreateView):
    model = Commentary
    template_name = 'forum/form_post.html'
    fields = ['message']
    success_url = reverse_lazy('forum:list_commentary')

    def form_valid(self, form):

        # Get category that post belongs to
        form.instance.category = Commentary.objects.get(pk=self.kwargs.get('pk'))
        form.instance.created_by = self.request.user
        form.save()

        # Save slug with post title
        form.instance.slug = slugify(
            str(form.instance.id) +
            "-" +
            form.instance.title
        )
        form.save()

        return super(CommentaryCreateView, self).form_valid(form)


class CommentaryDeleteView (DeleteView):
    model = Commentary
    success_url = reverse_lazy('forum:list_categories')

    def get_object(self):
        commentary = Commentary.objects.get(
            pk=self.kwargs.get('commentary_pk')
        )
        return commentary

    def get_success_url(self):
        return super(CommentaryDeleteView, self).get_success_url()


class CommentaryUpdateView(UpdateView):
    model = Commentary
    template_name = 'forum/form_commentary.html'
    fields = ['message']
    success_url = reverse_lazy('forum:list_post')

    def get_object(self):
        commentary = Commentary.objects.get(
            pk=self.kwargs.get('commentary_pk')
        )
        return commentary

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
        return super(CommentaryUpdateView, self).form_valid(form)


