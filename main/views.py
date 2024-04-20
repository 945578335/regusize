from django.shortcuts import render
import requests

def login(request):
    return render(request, "mainpage.html")
