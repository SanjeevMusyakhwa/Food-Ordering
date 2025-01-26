from django.urls import path
from .views import HomeView, CategoryList, FoodsList
urlpatterns = [
    path('', HomeView, name='home'),
    path('category/', CategoryList, name='category'),
    path('foods/', FoodsList, name='food'),

]
