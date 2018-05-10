from django import forms
from drdown.forum.models.model_commentary import Commentary
from drdown.forum.models.model_post import Post
from pagedown.widgets import PagedownWidget


class ComentaryForm(forms.ModelForm):

    message = forms.CharField(widget=PagedownWidget())

    class Meta:
        model = Commentary
        fields = ["message"]


class PostForm(forms.ModelForm):

    message = forms.CharField(widget=PagedownWidget())

    class Meta:
        model = Post
        fields = ["title", "message"]
