from django.shortcuts import render
from .models import Teachers
from apps.settings.models import Setting

# Create our views here.
def teacher_detail(request):
    setting = Setting.objects.latest('id')
    team = Teachers.objects.all()

    context = {
        'setting' : setting,
        'team' : team,
    }
    return render(request,'schooll/team.html', context)