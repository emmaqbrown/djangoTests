from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, TemplateView

from .models import *

# Create your views here.

class FoodList(ListView):

    template_name = 'food/foodList.html'

    def get_queryset(self):
            return Food.objects.all()