from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from Social import models


# Create your views here.
class wall(LoginRequiredMixin,ListView):
    queryset = models.Post.objects.all()
    context_object_name = 'posts'
    template_name = 'Social/wall.html'
    login_url = 'auth/login'