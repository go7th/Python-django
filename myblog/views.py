from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.
def mytest(request):
    article = models.Article.objects.get(pk=1)
    return render(request,'myblog/index.html',{'article':article})
    pass