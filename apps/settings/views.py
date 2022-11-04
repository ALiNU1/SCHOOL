from django.shortcuts import render
from .models import Setting
from apps.main.models import News,About
from apps.teachers.models import Teachers

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    about = About.objects.latest('id')
    news = News.objects.all()
    teachers = Teachers.objects.all()
    context = {
        'setting' : setting,
        'news' : news,
        'teachers' : teachers,
        'about': about,
    }

    return render(request, 'schooll/index1.html', context)