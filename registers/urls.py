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
    path('home/list_stores/', login_required(List_stores_view.as_view()), name='view_list_stores'),
    path('home/list_stores/edit_stores/<int:pk>/', login_required(Update_Store_View.as_view()), name='view_edit_stores'),
    path('home/list_stores/delete_stores/<int:pk>/', login_required(Delete_Store_View.as_view()), name='view_delete_stores'),
    path('new_store/',login_required(New_Store_View.as_view()),name='view_new_store'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]