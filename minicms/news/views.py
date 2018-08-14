from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Column,Article

from django.shortcuts import redirect

# def index(request):
#     return HttpResponse(u'欢迎来自强学堂学习Django')
 
 
# def column_detail(request, column_slug):
#     return HttpResponse('column slug: ' + column_slug)
 
 
# def article_detail(request, article_slug):
#     return HttpResponse('article slug: ' + article_slug)

def index(request):
    home_display_columns = Column.objects.filter(home_display=True)
    nav_display_columns = Column.objects.filter(nav_display=True)
 
    return render(request, 'index.html', {
        'home_display_columns': home_display_columns,
        'nav_display_columns': nav_display_columns,
    })
    # columns = Column.objects.all()
    # return render(request, 'index.html', {'columns': columns})

def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    return render(request, 'news/column.html', {'column': column})
 

# def article_detail(request, article_slug):
#     article = Article.objects.get(slug=article_slug)
#     return render(request, 'news/article.html', {'article': article})

def article_detail(request, pk, article_slug):
    article = Article.objects.get(pk=pk)
    if article_slug != article.slug:
        return redirect(article, permanent=True)
 
    return render(request, 'news/article.html', {'article': article})