from django.db import models
from drdown.users.models.model_user import User
from .model_post import Post


class Commentary(models.Model):
    message = models.TextField(max_length=4000)
    post = models.ForeignKey(Post, related_name='commentaries', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='commentaries', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=40)

    class Meta:
        verbose_name = "Commentary"
        verbose_name_plural = "Commentaries"
