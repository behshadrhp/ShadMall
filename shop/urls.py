from django.urls import path
from shop import views


app_name = 'shop'

urlpatterns = [
    path('', views.ProductView.as_view(), name='product_list'),
    path('category/<slug:category_slug>/', views.ProductView.as_view(), name='product_list_by_category'),
    path('detail/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
]
