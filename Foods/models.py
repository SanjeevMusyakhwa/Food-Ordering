from django.db import models

class CategoryModel(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Category Name')
    image = models.ImageField(upload_to='categories/', default='default.jpg')

  

    def __str__(self):
        return self.name


class FoodsModel(models.Model):
    title = models.CharField(max_length=255, verbose_name='Food Title')
    price = models.PositiveBigIntegerField(default=0)
    images = models.FileField(upload_to='foods/', default='foods.png')
    description = models.TextField()
    rating = models.FloatField(default=0.0, verbose_name='Rating')  # A field to store the rating (e.g., 0.0 to 5.0)
    review = models.TextField(blank=True, verbose_name='Review')    # A field to store the review text
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, related_name='foods')

    def __str__(self):
        return self.title
