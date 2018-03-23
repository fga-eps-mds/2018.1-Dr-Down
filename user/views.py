from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import User
from .forms import UserForm


def list_users(request):
    users = User.objects.all()
    return render(request, 'user/users.html', {'users': users})


def create_user(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_users')

    return render(request, 'user/users-form.html', {'form': form})


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
