from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import UserInfo
from .forms import CreateNewList

# Create your views here.
def index (response,id):
    ls=UserInfo.objects.get(id=id)
    return HttpResponse(response,"ins/base.html",{"ls":ls})

def home(response):
    return render(response,"ins/home.html",{})

def create(response):
    if response.method=="POST":
        form=CreateNewList(response.POST)

        if form.is_valid():
            n=form.cleaned_data["name"]
            t=UserInfo(name=n)
            t.save()
        return HttpResponseRedirect("/%i" %t.id)

    else:
        form=CreateNewList()
    return render(response,"ins/create.html",{"form":form})

#def 