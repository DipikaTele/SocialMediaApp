from django.urls import path
from Social import views

urlpatterns = [
    path('', views.wall.as_view()),
    path('home/',views.Home.as_view())
]


