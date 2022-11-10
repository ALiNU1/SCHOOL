from django.shortcuts import render,redirect
from apps.settings.models import Setting
from .models import News,About

# Create your views here.
def news_detail(request, id):
    setting = Setting.objects.latest('id')
    detail = News.objects.get(id=id)

    context = {
        'setting' : setting,
        'detail' : detail,
    }

    return render(request, 'schooll/detail.html', context)

def about(request):
    setting = Setting.objects.latest('id')
    about = About.objects.latest('id')

    context = {
        'setting' : setting,
        'about' : about
    }
    return render(request, 'schooll/about.html', context)