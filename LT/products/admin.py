from django.contrib import admin
from .models import *

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'brend_models', 'description', 
                    'price', 'image', 'category', 'is_available',
                    'quantity', 'size')
    list_display_links = ('brand', 'brend_models') 
    search_fields = ('brand', 'price', 'category', 'is_available', 'size')
    list_editable = ('description', 'price', 'category', 'image', 'quantity', 'is_available', 'size')
    list_filter = ('price', 'brand', 'is_available', 'quantity', 'size')
    prepopulated_fields = {"slug": ('brand', 'brend_models')}
    
class ProductcategorysAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('name', ) 
    search_fields = ('name', )
    prepopulated_fields = {"slug": ('name', )}

admin.site.register(Product, ProductsAdmin)
admin.site.register(ProductCategory, ProductcategorysAdmin)
