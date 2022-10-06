from django.shortcuts import redirect, render
from django.core.cache import cache
from rest_framework.decorators import api_view
from .bot import bot

def index(request):
    cache.clear()
    template = 'main/index.html'
    return render(request, template)

@api_view(['POST'])
def send_form(request):
    if request.method == 'POST':
        bot(request.data)
    else:
        return redirect('http://http://51.250.82.213/')