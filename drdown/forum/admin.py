from django.contrib import admin
from .models.model_category import Category
from .models.model_post import Post
from .models.model_commentary import Commentary

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Commentary)
