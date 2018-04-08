from django.db import models
from drdown.users.models import User
from .model_category import Category


class Post(models.Model):
    title = models.CharField(max_length=50)
    message = models.TextField(max_length=4000)
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=40)

    def __str__(self):
        return self.title


