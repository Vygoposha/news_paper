from django.db import models
from django.core.validators import MinValueValidator


#create product model
class Product(models.Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.TextField()
    quantity = models.IntegerField(validators=[MinValueValidator(0)])

    #ссылка на модель категории
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='products')
    # все продукты в категории будут доступны через поле products
    price = models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f'{self.name.title()}:{self.description[:20]}'

#  создаём категорию, к которой будет привязываться товар
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)  # названия категорий тоже не должны повторяться

    def __str__(self):
        return f'{self.name.title()}'
