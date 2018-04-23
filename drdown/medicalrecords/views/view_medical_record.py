from django.shortcuts import render
from ..models.model_medical_record import MedicalRecord
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.utils import timezone


class MedicalRecordsListView(ListView):
    model = MedicalRecord

# def get_context_data(self, **kwargs):
#     context = super(MedicalRecordsListView, self).get_context_data(**kwargs)
#     context['post'] = Post.objects.get(pk=self.kwargs.get('post_pk'))
#     return context

# def get_queryset(self):
#    post = Post.objects.get(pk=self.kwargs.get('post_pk'))
#    queryset = Commentary.objects.filter(post=post)
#    return queryset
