from django.shortcuts import render
from app.models import *
from django.http import HttpResponse

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

def insert_topic(request):
    tn=input('enter topicname;')
    NTO=Topic.objects.get_or_create(Topic_Name=tn)[0]
    NTO.save()
    return HttpResponse('Topic is created')


def insert_webpage(request):
    tn=input('enter topic name:')
    n=input('enter name:')
    u=input('enter url:')
    e=input('enter email:')
    TO=Topic.objects.get(Topic_Name=tn)
    NWO=Webpage.objects.get_or_create(Topic_Name=TO,Name=n,Url=u,Email=e)[0]
    NWO.save()
    return HttpResponse('Webpage is created')


def insert_accessrecord(request):
    pk=int(input('enter pk value of webpage:'))
    d=input('enter date:')
    a=input('enter author:')
    WO=Webpage.objects.get(pk=pk)
    NAO=AccessRecord.objects.get_or_create(Name=WO,Date=d,Author=a)[0]
    NAO.save()
    return HttpResponse('Acessrecord is created')