from collections.abc import Mapping
from typing import Any
from django import forms
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserModel, AuthenticationForm
from .models import *


class AddProductForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Категория не выбрана"
        self.fields['description'].widget.attrs['style'] = "width:500px"
        
        
    class Meta:
        model = Product
        fields = ['brand','brend_models', 'description', 'image', 'price', 'slug', 'category', 'quantity', 'is_available', 'size']
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form__input'}),
            'brend_models': forms.TextInput(attrs={'class': 'form__input'}),
            'description': forms.Textarea(attrs={'size': 120, 'class': "form__input-filter"}),
            'price': forms.NumberInput(attrs={'class': 'form__input'}),
            'category': forms.Select(attrs={'class': 'form__input'}),
            'quantity': forms.NumberInput(attrs={'class': 'form__input'}),
            'size': forms.NumberInput(attrs={'class': 'form__input', 'step':0.5}),
        }
        
    def clean_brand(self): #  Пользовательская валидация
        brand = self.cleaned_data['brand']
        if len(brand)>200:
            raise forms.ValidationError("Длинна превышает 200 символов")
        return brand
    
    def clean_size(self): #  Пользовательская валидация
        size = self.cleaned_data['size']
        if float(size)<0:
            raise forms.ValidationError("Слишком маленький размер")
        return size
    
    def clean_price(self): #  Пользовательская валидация
        price = self.cleaned_data['price']
        if float(price)<0:
            raise forms.ValidationError("Отрицательная цена")
        return price
    

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form__input-reg'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form__input-reg'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form__input-reg'}))
    password2 = forms.CharField(label='Пароль повтор', widget=forms.PasswordInput(attrs={'class': 'form__input-reg'}))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widget = {
            'username': forms.TextInput(attrs={'class': 'form__input-reg'}),
            'password1': forms.PasswordInput(attrs={'class': 'form__input-reg'}),
            'password2': forms.PasswordInput(attrs={'class': 'form__input-reg'}),
        }
        

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form__input-reg'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form__input-reg'}))
    
    
class FilterProductForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
    size = forms.DecimalField(label='Размер', decimal_places=2, required=False, widget=forms.NumberInput(attrs={"class":"form__input-filter", 'size': '40', 'step':0.5})) 
    brand = forms.CharField(label='Бренд', widget=forms.TextInput(attrs={'class': 'form__input-filter'}), required=False)
    
    class Meta:
        model = Product
        fields = ('size', 'brand')

