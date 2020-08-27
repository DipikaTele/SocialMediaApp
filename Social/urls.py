from django.urls import path
from Social import views

urlpatterns = [
    path('home/',views.Home.as_view()),
    path('',views.wall.as_view())
]


