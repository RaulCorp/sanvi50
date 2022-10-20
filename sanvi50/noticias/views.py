from django.shortcuts import render

from noticias.models import Noticia
from .models import Noticia


# Create your views here.
def portfolio(request):
    noticias= Noticia.objects.all()
    return render(request,'noticias/portfolio.html', {'noticias':noticias})