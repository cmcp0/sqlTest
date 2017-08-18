from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import logging
from app.models import *

# Create your views here.

def tabla(request):
    logging.info("!")
