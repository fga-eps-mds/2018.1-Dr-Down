from ..models.model_category import Category
from django.views.generic import ListView


class CategoryListView(ListView):
    model = Category
    slug_field = 'name'
    slug_url_kwarg = 'name'


