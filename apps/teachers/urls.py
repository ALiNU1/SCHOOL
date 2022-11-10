from django.urls import path
from .views import teacher_detail

urlpatterns = [
    path('team/', teacher_detail, name='team'),
]