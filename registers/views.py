from django.shortcuts import render, redirect

from django.http import HttpResponseRedirect

from django.contrib.auth.decorators import login_required

from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.models import User

from django.urls import reverse_lazy

from .forms import *

from .models import *

from django.views.generic import View, TemplateView, ListView, UpdateView, CreateView, DetailView, DeleteView

from rest_framework import viewsets

from .serializers import *

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/home/')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None and user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/home/')
        form = LoginForm()
        ctx = {'form': form}
        return render(request, 'login.html', ctx)
        
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required(login_url='')
def home_view(request):
    products = Product.objects.all()
    ctx = {'products':products}
    return render(request, 'index.html', ctx)
    
def register_view(request):
    info = "INICIANDO"
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            print('entramos3')
            user = form.save()
            profile = Cashier()
            profile.user = user
            profile.phone = form.cleaned_data['phone']
            profile.direction = form.cleaned_data['direction']
            profile.box = form.cleaned_data['box']
            profile.state = form.cleaned_data['state']
            profile.image = form.cleaned_data['image']
            profile.save()
            info = "GUARDADO CON EXITO"
            ctx = {'info': info}
            return render(request, 'login.html', ctx)
        else:
            print('Form Incorrecto')
    else:
        form = ProfileForm()
        form.fields['username'].help_text = None
        form.fields['password1'].help_text = None
        form.fields['password2'].help_text = None

    ctx = {'form':form,'info':info}
    return render(request, 'register.html', ctx)

# STORE

class List_stores_view(ListView):
    model = Store
    template_name = 'list_stores.html'
    queryset = Store.objects.filter(state=True)
    context_object_name = 'stores'

class New_Store_View(CreateView):
    model = Store
    form_class = StoreForm
    template_name = 'new_store.html'
    success_url = reverse_lazy('view_list_stores')

class Update_Store_View(UpdateView):
    model = Store
    form_class = StoreForm
    template_name = 'update_store.html'
    success_url = reverse_lazy('view_list_stores')
    
class Delete_Store_View(DetailView):
    model = Store
    template_name = 'delete_store.html'
    def post(self,request,pk,*args,**kwargs):
        object = Store.objects.get(id=pk)
        object.state = False
        object.save()
        return redirect('view_list_stores')

# PRODUCTS

class List_products_view(ListView):
    model = Product
    template_name = 'list_products.html'
    queryset = Product.objects.filter(state=True)
    context_object_name = 'products'

# class New_Product_View(CreateView):
#     model = Product
#     form_class = ProductForm
#     template_name = 'new_product.html'
#     success_url = reverse_lazy('view_list_products')

@login_required(login_url='')
def New_Product_View(request):
    if request.method == 'POST':
        form = ProductForm(request.POST,request.FILES)
        ctx = {'form': form}
        if form.is_valid():
            form.save()
            return redirect('/home/list_products/')
    else:
        form = ProductForm()
        ctx = {'form': form}
    return render(request,'new_product.html',ctx)

class Update_Product_View(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'update_product.html'
    success_url = reverse_lazy('view_list_products')
    
class Delete_Product_View(DetailView):
    model = Product
    template_name = 'delete_product.html'
    def post(self,request,pk,*args,**kwargs):
        object = Product.objects.get(id=pk)
        object.state = False
        object.save()
        return redirect('view_list_products')


# CLASS REST framework

class StoreViewSet(viewsets.ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class CashierViewSet(viewsets.ModelViewSet):
    queryset = Cashier.objects.all()
    serializer_class = CashierSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
