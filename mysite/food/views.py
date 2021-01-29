from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, FormView
from .forms import FoodForm
from .models import *

# Create your views here.

class FoodList(ListView):

    template_name = 'food/foodList.html'
    model = Food
    paginate_by = 3
    context_object_name = 'foods'

    def get_queryset(self):
        #Filters archived foods out of main list 
        return self.model.objects.filter(archive=False)

class ArchivedFoodList(ListView):

    template_name = 'food/archivedFoodList.html' 
    model = Food
    paginate_by = 12
    context_object_name = 'foods'

    def get_queryset(self):
        #Filters archived foods out of main list 
        return self.model.objects.filter(archive=True)


class FoodForm(FormView):
    template_name = 'food/foodForm.html'
    form_class = FoodForm
    success_url = '/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)

        
  