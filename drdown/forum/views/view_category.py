from ..models.model_category import Category
from django.views.generic import ListView
from ..views.view_base import BaseViewTemplate


class CategoryListView(BaseViewTemplate, ListView):
    model = Category
    slug_field = 'name'
    slug_url_kwarg = 'name'

