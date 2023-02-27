from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.core.mail import send_mail
#from .forms import *

def home(request):
    return render(request, 'landing_page/index.html')