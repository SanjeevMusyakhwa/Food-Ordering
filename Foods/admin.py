from django.contrib import admin
from .models import CategoryModel, FoodsModel

@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(FoodsModel)
class FoodsAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'rating')
