from django.urls import path
from .views import list_users, create_user, update_user

urlpatterns = [
    path('', list_users, name='list_users'),
    path('new/', create_user, name='create_user'),
    path('edit/<int:id>', update_user, name='update_user')

]
