from django import forms 
from .models import Task 
  
# create a ModelForm 
class TaskForm(forms.ModelForm): 
    class Meta: 
        model = Task 
        fields = ('label','quantity','notes')