from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('posts/', views.postsHandler),
    # path('posts/<int:pk>', views.postHandler)
]   