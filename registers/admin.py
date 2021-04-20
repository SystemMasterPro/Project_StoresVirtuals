from django.contrib import admin

from .models import *

from import_export import resources

from import_export.admin import ImportExportModelAdmin

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

class CategoryAdmin(ImportExportModelAdmin):
    list_display = ('name', 'description', 'store')
    readonly_fields = ('created', 'updated')
    search_fields = ['name']
    resource_class = CategoryResource

class StoreResource(resources.ModelResource):
    class Meta:
        model = Store

class StoreAdmin(ImportExportModelAdmin):
    list_display = ('name', 'direction', 'phone')
    readonly_fields = ('created', 'updated')
    search_fields = ['name']
    resource_class = StoreResource

class ProductResource(resources.ModelResource):
    class Meta:
        model = Product

class ProductAdmin(ImportExportModelAdmin):
    list_display = ('product', 'price', 'state','image_product','category')
    readonly_fields = ('created', 'updated')
    search_fields = ['product']
    resource_class = ProductResource

class SupplierResource(resources.ModelResource):
    class Meta:
        model = Supplier

class SupplierAdmin(ImportExportModelAdmin):
    list_display = ('name', 'phone', 'state','store')
    readonly_fields = ('created', 'updated')
    search_fields = ['name']
    resource_class = SupplierResource

class CashierResource(resources.ModelResource):
    class Meta:
        model = Cashier

class CashierAdmin(ImportExportModelAdmin):
    list_display = ('user', 'phone', 'direction','box','state','image_profile','store')
    readonly_fields = ('created', 'updated')
    search_fields = ['user']
    resource_class = CashierResource

class ClientResource(resources.ModelResource):
    class Meta:
        model = Client

class ClientAdmin(ImportExportModelAdmin):
    list_display = ('name', 'lastName', 'direction','phone','state','store')
    readonly_fields = ('created', 'updated')
    search_fields = ['name']
    resource_class = ClientResource

class SaleResource(resources.ModelResource):
    class Meta:
        model = Sale

class SaleAdmin(ImportExportModelAdmin):
    list_display = ('id', 'value_final', 'date', 'client')
    resource_class = SaleResource

admin.site.register(Category, CategoryAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Cashier, CashierAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Sale, SaleAdmin)
