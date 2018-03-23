from django.urls import path
from .views import list_users, create_user, UpdateUserView, UserDeleteView

urlpatterns = [
    path('', list_users, name='list_users'),
    path('new/', create_user, name='create_user'),
    path('edit/<int:pk>', UpdateUserView.as_view(), name='update_user'),
    path('delete/<int:pk>', UserDeleteView.as_view(), name='delete_user'),

]
