from django.shortcuts import render,redirect
from .models import User


def list_users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})
