from django import forms

from .models import *

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(render_value=False))

    class Meta:
        model = User
        fields = ['username', 'password']
        
class ProfileForm(UserCreationForm):
    phone= forms.CharField(widget=forms.TextInput())
    direction = forms.CharField(widget=forms.TextInput())
    box = forms.CharField(widget=forms.TextInput())
    state = forms.CharField(widget=forms.TextInput())
    image = forms.ImageField()

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'direction', 'phone']
        labels = {
            'name': 'Nombre de la Tienda:',
            'direction': 'Direccion de la Tienda:',
            'phone': 'Telefono de la Tienda:'
        }
        widget = {
            'name': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Nombre de la Tienda',
                    'id':'name'
                }
            ),
            'direction': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Direccion de la Tienda',
                    'id':'direction'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Telefono de la Tienda',
                    'id':'phone'
                }
            )
        }
    
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product','price','state','image','category']
        labels = {
            'product': 'Nombre del Producto:',
            'price':'Precio del Producto:',
            'image': 'Imagen:',
            'category':'Categoria:'
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','description','store']
        labels = {
            'name': 'Nombre de la Categoria:',
            'description':'Descripcion:',
            'store': 'Tienda:'
        }    