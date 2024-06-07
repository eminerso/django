from django.shortcuts import render 
from django.http import HttpResponse
from .models import Sual 


# Create your views here.
def my_home(request):
    questions=Sual.objects.all()
    return render(request,"home.html",{'questions':questions})

def items_page(request):
    return render(request,"section/gf.html")
