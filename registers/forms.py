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

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name','phone','store']
        labels = {
            'name': 'Nombre del Proveedor:',
            'phone':'Telefono del Proveedor:',
            'store': 'Tienda:'
        }

class CashierForm(forms.ModelForm):
    class Meta:
        model = Cashier
        fields = ['user','phone','direction','box','image','store']
        labels = {
            'user': 'Nombre del Cajero:',
            'phone':'Telefono:',
            'direction': 'Direccion:',
            'box':'Caja:',
            'image':'Imagen:',
            'store':'Tienda'
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name','lastName','direction','phone','store']
        labels = {
            'name':'Nombre del Cliente:',
            'lastName':'Apellido del Cliente:',
            'direction':'Direccion del Cliente:',
            'phone':'Telefono del Cliente:',
            'store':'Tienda del Cliente:'
        }

class SaleForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ['value_final','client']
        labels = {
            'value_final':'Valor Total:',
            'client':'Cliente:'
        }    