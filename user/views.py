from django.shortcuts import render, redirect
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


def update_user(request, id):
    user = User.objects.get(id=id)
    form = UserForm(request.POST or None, instance=user)

    if form.is_valid():
        form.save()
        return redirect('list_users')

    return render(
     request,
     'user/users-form.html',
     {'form': form, 'user': user}
     )
