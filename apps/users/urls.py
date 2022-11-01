from django.urls import path
from .views import signup
from . import views

urlpatterns = [ 
    path('register/', views.signup, name = 'register'),
]