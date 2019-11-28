from django.shortcuts import render
from django.http import HttpResponse

from .models import About

# Create your views here.
def about(request):
    about = About.objects.get(id=2)
    return render(request, "about.html", {'abouts':about})
