from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from apps.settings.models import Setting

def signup(request):
    setting = Setting.objects.latest('id')
    context = {
        'setting' : setting,
    }
    return render(request, 'users/register.html', context)