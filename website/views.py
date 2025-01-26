from django.shortcuts import render
from Foods.models import FoodsModel, CategoryModel
# Create your views here.

def HomeView(request):
  categories = CategoryModel.objects.all()
  foods = FoodsModel.objects.all()
  return render(request, 'index.html',{'foods': foods, 'categories':categories})
