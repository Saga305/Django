"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
import random

def ring(request):
    return render(request, "ring.html")

def bar(request):
    return render(request, "bar.html")

def color(request):
    return render(request, "color.html")

def ball(request):
    return render(request, "ball.html")

def render_with_context(request):
    return render(request, "rotate_on_axis.html")

def stop_watch(request):
    return render(request, "stop_watch.html")

def login(request):
    return render(request, "login.html")

def types(request):
    context = {
        'dictionary': {"name":"Ajay"},
        'integer':555,
        'lst':["The", "Great", "Saga"],
        'tpl':("Apna", "time", "kab", "aayega!!!")
    }
    return render(request, "types.html", context)


def django_template_lang(request):
    data = {
        'sachin': 101,
        'rony':55,
        'jadeja':25,
        'dube':43
    }
    color = random.choice(["blue", "red", "black", "yellow", "green", "pink"])
    return render(request, "django_template_lang.html",context={"data":data, "color":color})

urlpatterns = [
    path('ring/', ring),
    path('rotate/', render_with_context),
    path('color/', color),
    path('ball/', ball),
    path('stop_watch/', stop_watch),
    path('bar/', bar),
    path('login/', login),
    path('types/', types),
    path('django_template_lang/', django_template_lang),
]
