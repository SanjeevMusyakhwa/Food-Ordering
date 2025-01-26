from django.shortcuts import render
from Foods.models import FoodsModel, CategoryModel

def HomeView(request):
    search_query = request.GET.get('search', '')  # Get the search query from the request
    food_type = request.GET.get('food_type', '')  # Get the food type from the request
    
    categories = CategoryModel.objects.all()[:5]
    
    if search_query:
        foods = FoodsModel.objects.filter(title__icontains=search_query)[:10]
    else:
        foods = FoodsModel.objects.all()[:10]
    
    # Filter by food type if specified
    if food_type:
        foods = foods.filter(food_type=food_type)
    
    return render(request, 'index.html', {'foods': foods, 'categories': categories})
