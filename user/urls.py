from django.urls import path
from .views import list_users, create_user

urlpatterns = [
    path('', list_users, name='list_users'),
    path('new/', create_user, name='create_user'),

]
