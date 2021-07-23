from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

def bank(request):
    return HttpResponse("Currency Bank's")
