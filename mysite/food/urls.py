from django.urls import path
from . import views


urlpatterns = [
    # path('', views.index),
    path('', views.FoodList.as_view(), name='food-list'),
    path('newfood/', views.FoodForm.as_view(), name='new-food'),
    # path('<int:pageno>/', views.FoodList.as_view(), name='food-list'),

]
