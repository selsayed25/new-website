from django.urls import path
from . import views

urlpatterns = [
    path("", views.blogIndex, name="blogIndex"),
    path("posts/<int:pk>/", views.blogDetail, name="blogDetail"),
    path("category/<str:category>/", views.blogCategory, name="blogCategory"),
]