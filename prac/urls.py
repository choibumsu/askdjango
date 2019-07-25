from django.urls import path
from . import views

app_name = 'prac'

urlpatterns = [
    path('new/', views.post_new),
    path('<int:id>/edit/', views.post_edit),
]