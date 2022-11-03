from multiprocessing import context
from django.shortcuts import render,redirect
from apps.settings.models import Setting
from .models import News

# Create your views here.
def news_detail(request, id):
    setting = Setting.objects.latest('id')
    detail = News.objects.get(id=id)

    context = {
        'setting' : setting,
        'detail' : detail,
    }

    return render(request, 'schooll/detail.html', context)