# shop/urls.py

from django.urls import path
from .views import (
    ProductListView,
    OrderCreateView,
    ProductAdminListCreateView,
    ProductAdminDetailView,
    OrderAdminListView,
    OrderStatusUpdateView,
    order_search_view,
    statistics_view,
)

urlpatterns = [
    # ========== FOYDALANUVCHI ==========
    path('products/', ProductListView.as_view(), name='product-list'),
    path('orders/', OrderCreateView.as_view(), name='order-create'),

    # ========== ADMIN ==========
    path('admin/products/', ProductAdminListCreateView.as_view(), name='admin-product-list-create'),
    path('admin/products/<int:pk>/', ProductAdminDetailView.as_view(), name='admin-product-detail'),

    path('admin/orders/', OrderAdminListView.as_view(), name='admin-order-list'),
    path('admin/orders/<int:pk>/status/', OrderStatusUpdateView.as_view(), name='admin-order-status-update'),

    path('admin/orders/search/', order_search_view, name='admin-order-search'),
    path('admin/statistics/', statistics_view, name='admin-statistics'),
]
