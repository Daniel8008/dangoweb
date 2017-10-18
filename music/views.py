
from django.http import HttpResponse,Http404

from models import Albums, songs
from django.shortcuts import render



def index(request):
    myAlbums =Albums.objects.all()

    return render(request,'music/index.html',{'myAlbums': myAlbums})

def detail(request,album_id):

    try:
        album=Albums.objects.get(pk=album_id)
    except Albums.DoesNotExist:
        raise  Http404("Sorry album does not exist..please try somethiing else")
    return render(request,'music/details.html',{'album':album})