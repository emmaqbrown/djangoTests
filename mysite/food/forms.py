from django import forms 
from .models import Food 
  
# create a ModelForm 
class FoodForm(forms.ModelForm): 
    class Meta: 
        model = Food 
        fields = ('label','quantity')