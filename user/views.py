from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView, CreateView, ListView
from django.urls import reverse_lazy
from .models import User
from .forms import UserForm


class ListUserView(ListView):
    model = User
    template_name = 'user/users.html'


class CreateUserView(CreateView):
    model = User
    template_name = 'user/users-form.html'
    form_class = UserForm
    success_url = '/'


class UpdateUserView(UpdateView):
    model = User
    template_name = 'user/users-form.html'
    form_class = UserForm
    success_url = '/'


class UserDeleteView(DeleteView):
    """
    Class to delete a user from database
    """
    model = User
    success_url = reverse_lazy('list_users')
    template_name = 'user/user_confirm_delete.html'
