"""dangoweb URL Configuration

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
from django.conf.urls import include, url, patterns
from django.conf.urls.static import static
from django.contrib import admin

from dangoweb import settings
from music.views import index,detail

urlpatterns = patterns( '',url(r'^admin/', include(admin.site.urls)),
    url(r'^home/$', index),
    url(r'^home/music/(\d{1,3})$',detail)
) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



