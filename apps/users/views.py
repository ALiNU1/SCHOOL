from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from apps.settings.models import Setting
from django.http import HttpResponse
from .models import User

def signup(request):
    setting = Setting.objects.latest('id')
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        profile_image = request.FILES.get('profile_image')
        if password1 == password2:
            user = User.objects.create(name = name, profile_image = profile_image, email = email)
            user.set_password(password1)
            user.save()
            user = User.objects.get(name = name)
            user = authenticate(name = name, password = password1)
            login(request, user)
            return redirect('index')
           
        else:
            return HttpResponse("Пароли не совпадают")

    context = {
        'setting' : setting,
    }
    return render(request, 'users/register.html', context)