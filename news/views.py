from django.shortcuts import render, redirect
from django.urls import reverse
from .models import NewsM, Rubric
from .parser import current_day_news


def newsp(request):
    # a = current_day_news(2)
    # for key, val in a.items():
    #     try:
    #         val["id"] = NewsM.objects.create(title=val["title"], content=val["fulltext"], image_links=val["imgs"], date=val["news_date"])
    #     except:
    #         pass
    all_news = NewsM.objects.all()
    return render(request, "news.html", {'news': all_news})