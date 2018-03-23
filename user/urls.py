from django.urls import path
from .views import ListUserView, CreateUserView
from .views import UpdateUserView, UserDeleteView

urlpatterns = [
    path('', view=ListUserView.as_view(), name='list_users'),
    path('new/', view=CreateUserView.as_view(), name='create_user'),
    path('edit/<int:pk>', UpdateUserView.as_view(), name='update_user'),
    path('delete/<int:pk>', UserDeleteView.as_view(), name='delete_user'),

]
