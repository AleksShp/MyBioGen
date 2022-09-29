from django.shortcuts import render
from django.core.cache import cache

def index(request):
    cache.clear()
    template = 'main/index.html'
    return render(request, template)

    #href="../static/pdf/booklet_MyBiogen.pdf" target="_blank"
