from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index),
    path('form/', views.send_form),
]