
from django.shortcuts import render
import random

def django_template_lang(request):
    data = {
        'sachin': 101,
        'rony':55,
        'jadeja':25,
        'dube':43
    }
    color = random.choice(["blue", "red", "black", "yellow", "green", "pink"])
    return render(request, "django_template_lang.html",context={"data":data, "color":color})