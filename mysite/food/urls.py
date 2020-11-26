from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index),
    path('', views.FoodList.as_view(), name='my-view'),
]
