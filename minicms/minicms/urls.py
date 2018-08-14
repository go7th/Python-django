"""minicms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

from DjangoUeditor import urls as DjangoUeditor_urls
from . import settings

urlpatterns = [
    url(r'^$', 'news.views.index',name='index'),
    url(r'^column/(?P<column_slug>[^/]+)/$', 'news.views.column_detail', name='column'),
    # url(r'^news/(?P<article_slug>[^/]+)/$', 'news.views.article_detail', name='article'),
    url(r'^news/(?P<pk>\d+)/(?P<article_slug>[^/]+)/$', 'news.views.article_detail', name='article'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/',include('grappelli.urls')),

    url(r'^ueditor/', include('DjangoUeditor.urls' )),
    url( r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root':settings.STATIC_ROOT }),

]

from django.conf import settings
 
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)