from django.shortcuts import render
from app.models import *

# Create your views here.
def display_topic(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    return render(request,'display_topic.html',d)


def display_webpage(request):
    QLWO=Webpage.objects.all()
    d={'webpage':QLWO}
    return render(request,'display_webpage.html',d)


def display_accessrecord(request):
    QLAO=AccessRecord.objects.all()
    d={'accessrecord':QLAO}
    return render(request,'display_accessrecord.html',d)
