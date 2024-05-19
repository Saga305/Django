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
from naya_folder.dusra_folder.functions import django_template_lang

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

def stock(request):
    stock_info : list[dict] = [
        {
            "name":"ONGC",
            "market_price":279.00,
            "quantity":104,
            "buy_price":274.00,
            "returns":+520.00,
            "url": "https://groww.in/stocks/oil-natural-gas-corporation-ltd",
        },
        {
            "name":"Nippon India ETF Gold BeES",
            "market_price":62.89,
            "quantity":35,
            "buy_price":61.16,
            "returns":+60.55,
            "url":"https://groww.in/etfs/reliance-etf-gold-bees",
        },
        {
            "name":"NIFTYBEES",
            "market_price":249.05,
            "quantity":2,
            "buy_price":236.02,
            "returns":+26.06,
            "url":"https://groww.in/etfs/reliance-etf-nifty-bees",
        },
        {
            "name":"LIQUIDCASE",
            "market_price":102.26,
            "quantity":8,
            "buy_price":101.42,
            "returns":+6.72,
            "url":"https://groww.in/etfs/zerodha-nifty-d-rate-liquid-etf",
        },
        {
            "name":"JUNIORBEES",
            "market_price":720.17,
            "quantity":73,
            "buy_price":692.85,
            "returns":+1994.36,
            "url":"https://groww.in/etfs/reliance-etf-junior-bees",
        },
        {
            "name":"IRFC",
            "market_price":173.25,
            "quantity":22,
            "buy_price":157.00,
            "returns":+357.50,
            "url":"https://groww.in/stocks/indian-railway-finance-corporation-ltd",
        },
        {
            "name":"HDFC Bank",
            "market_price":1466.05,
            "quantity":9,
            "buy_price":1594.75,
            "returns":-1158.30,
            "url":"https://groww.in/stocks/hdfc-bank-ltd",
        },
    ]
    context = {
        'stock': stock_info,
    }
    return render(request, "stock.html", context)




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
    path('stock/', stock),
]
