from django.shortcuts import render
from django.views.generic import ListView
from Social import models


# Create your views here.
class wall(ListView):
    queryset = models.Post.objects.all()
    context_object_name = 'posts'
    template_name = 'Social/wall.html'