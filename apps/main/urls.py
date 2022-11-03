from django.urls import path
from .views import news_detail

urlpatterns = [
    path('detail/<int:id>', news_detail, name='news_detail'),
]