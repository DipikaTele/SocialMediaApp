from django.urls import path
from Social import views

urlpatterns = [
    path('', views.wall.as_view()),
    path('post/',views.Post.as_view()),
    path('home/', views.Home.as_view()),
    path('post/<int:pk>/like', views.PostLike.as_view()),
    path('post/<int:pk>/comment', views.PostComment.as_view())
]





