# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



def user_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.category, filename)


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name="Название", db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})
    
    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Категория" 
        verbose_name_plural = "Категории" 
        ordering = ['id', ]


class Product(models.Model):
    brand = models.CharField(max_length=256, verbose_name="Бренд")
    brend_models = models.CharField(max_length=256, verbose_name="Модель")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Цена")
    image = models.ImageField(upload_to=user_directory_path, verbose_name="Изображение")
    quantity = models.PositiveIntegerField(verbose_name="Количество", default=1)
    is_available = models.BooleanField(verbose_name="В наличии", default=True)
    size = models.DecimalField(verbose_name="Размер", decimal_places=1, max_digits=3)
    category = models.ForeignKey(to=ProductCategory, verbose_name=("Категория"), on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    
    
    def __str__(self) -> str:
        return self.brand + ' ' + self.brend_models
    
    def get_absolute_url(self):
        return reverse('item', kwargs={'item_slug': self.slug})
    
    class Meta:
        verbose_name = "Товар" 
        verbose_name_plural = "Товары" 
        ordering = ['brand','brend_models', 'category']
    