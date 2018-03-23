from django.urls import path
from .views import list_users, create_user, UpdateUserView

urlpatterns = [
    path('', list_users, name='list_users'),
    path('new/', create_user, name='create_user'),
    path('edit/<int:pk>', UpdateUserView.as_view(), name='update_user')

]
