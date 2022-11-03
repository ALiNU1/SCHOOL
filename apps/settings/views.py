from django.shortcuts import render
from .models import Setting
from apps.main.models import News
from apps.teachers.models import Teachers

# Create your views here.
def index(request):
    setting = Setting.objects.latest('id')
    news = News.objects.all()
    teachers = Teachers.objects.all()
    context = {
        'setting' : setting,
        'news' : news,
        'teachers' : teachers,
    }
    return render(request, 'schooll/index1.html', context)