from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib import messages
from mbapp.models import devices

def index(request):
        res = devices.objects.all()
        return render(request,'index.html', {"spisok":res})

def reg(request):
    if request.method == "POST":
        data = request.POST
        print(data["user"])
        print(data["password"])
        user = User.objects.create_user(username=data["user"], password=data["password"], email=data["email"])
        user.save()
    return render(request,'reg.html')


def auth(request):
    if request.method == "POST":
        data = request.POST
        user = authenticate(username=data["user"], password=data["password"])
        if user != None:
            return HttpResponse(f'Hello, {user}')
        else:
            messages.add_message(request, messages.INFO, 'Пароль неверный.')
    return render(request,'auth.html')

def card(request, id):
        res = devices.objects.filter(id = id)
        return render(request,'card.html', {"data":res})

