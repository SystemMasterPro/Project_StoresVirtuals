from django.urls import include, path

from .views import *

from . import views

from rest_framework import routers

from django.contrib.auth.decorators import login_required

router = routers.DefaultRouter()
router.register('stores', views.StoreViewSet)
router.register('clients', views.ClientViewSet)
router.register('products', views.ProductViewSet)
router.register('sales', views.SaleViewSet)
router.register('cashiers',views.CashierViewSet)
router.register('categories',views.CategoryViewSet)
router.register('suppliers',views.SupplierViewSet)


urlpatterns = [
    path('', login_view, name='view_login'),
    path('home/', home_view, name='view_home'),
    path('logout/', logout_view, name='view_logout'),
    path('register/', register_view, name='view_register'),
    # STORES URL
    path('home/list_stores/', login_required(List_stores_view.as_view()), name='view_list_stores'),
    path('home/list_stores/edit_stores/<int:pk>/', login_required(Update_Store_View.as_view()), name='view_edit_stores'),
    path('home/list_stores/delete_stores/<int:pk>/', login_required(Delete_Store_View.as_view()), name='view_delete_stores'),
    path('new_store/',login_required(New_Store_View.as_view()),name='view_new_store'),
    # PRODUCTS URL
    path('home/list_products/', login_required(List_products_view.as_view()), name='view_list_products'),
    path('home/list_products/edit_products/<int:pk>/', login_required(Update_Product_View.as_view()), name='view_edit_products'),
    path('home/list_products/delete_products/<int:pk>/', login_required(Delete_Product_View.as_view()), name='view_delete_products'),
    path('new_product/',New_Product_View, name='view_new_product'),
    # CATEGORIES URL
    path('home/list_categories/', login_required(List_categories_view.as_view()), name='view_list_categories'),
    path('home/list_categories/edit_categories/<int:pk>/', login_required(Update_Category_View.as_view()), name='view_edit_categories'),
    path('home/list_categories/delete_categories/<int:pk>/', login_required(Delete_Category_View.as_view()), name='view_delete_categories'),
    path('new_category/',login_required(New_Category_View.as_view()),name='view_new_category'),
    # SUPPLIERS URL
    path('home/list_suppliers/', login_required(List_suppliers_view.as_view()), name='view_list_suppliers'),
    path('home/list_suppliers/edit_suppliers/<int:pk>/', login_required(Update_Supplier_View.as_view()), name='view_edit_suppliers'),
    path('home/list_suppliers/delete_suppliers/<int:pk>/', login_required(Delete_Supplier_View.as_view()), name='view_delete_suppliers'),
    path('new_supplier/',login_required(New_Supplier_View.as_view()),name='view_new_supplier'),
    # CASHIERS
    path('home/list_cashiers/', login_required(List_cashiers_view.as_view()), name='view_list_cashiers'),
    path('home/list_cashiers/edit_cashiers/<int:pk>/', login_required(Update_Cashier_View.as_view()), name='view_edit_cashiers'),
    path('home/list_cashiers/delete_cashiers/<int:pk>/', login_required(Delete_Cashier_View.as_view()), name='view_delete_cashiers'),
    path('new_cashier/',New_Cashier_View, name='view_new_cashier'),
    # CLIENTS
    path('home/list_clients/', login_required(List_clients_view.as_view()), name='view_list_clients'),
    path('home/list_clients/edit_clients/<int:pk>/', login_required(Update_Client_View.as_view()), name='view_edit_clients'),
    path('home/list_clients/delete_clients/<int:pk>/', login_required(Delete_Client_View.as_view()), name='view_delete_clients'),
    path('new_client/',login_required(New_Client_View.as_view()),name='view_new_client'),
    # SALES
    path('home/list_sales/', login_required(List_sales_view.as_view()), name='view_list_sales'),
    path('home/list_sales/edit_sales/<int:pk>/', login_required(Update_Sale_View.as_view()), name='view_edit_sales'),
    path('home/list_sales/delete_sales/<int:pk>/', login_required(Delete_Sale_View.as_view()), name='view_delete_sales'),
    path('new_sale/',login_required(New_Sale_View.as_view()),name='view_new_sale'),
    # API-REST
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]