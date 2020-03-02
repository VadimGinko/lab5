from django.shortcuts import render
from django.http import HttpResponse


from django.shortcuts import get_object_or_404, render, redirect

from .models import Riddle


# главная страница со списком загадок
def index(request):
    message = None
    if "message" in request.GET:
        message = request.GET["message"]
    # создание HTML-страницы по шаблону index.html
    # с заданными параметрами latest_riddles и message
    return render(
        request,
        "index.html",
        {
            "latest_riddles":
                Riddle.objects.order_by('-Name'),
            "message": message
        }
    )


