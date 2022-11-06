from django.urls import path
from .views import news_detail,about

urlpatterns = [
    path('detail/<int:id>', news_detail, name='news_detail'),
    path('about/',about,name="about"),
]