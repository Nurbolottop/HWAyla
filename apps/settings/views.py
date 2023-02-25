from django.shortcuts import render

from .models import Settings,About

# Create your views here.
def index(request):
    setting  = Settings.objects.latest('id')
    
    context = {
        'setting':setting
    }
    
    return render(request,'02_index.html', context)

def about(request):
    setting  = Settings.objects.latest('id')
    about = About.objects.latest('id')
    
    context = {
        'setting':setting,
        'about':about
    }
    return render(request,'about.html',context)

def contact(request):
    setting  = Settings.objects.latest('id')
    
    context = {
        'setting':setting
    }
    
    return render(request,'contact.html', context)

