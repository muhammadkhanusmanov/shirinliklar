# shop/views.py

from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from .models import Product, Order
from .serializers import (
    ProductSerializer,
    ProductAdminSerializer,
    OrderCreateSerializer,
    OrderAdminSerializer,
    OrderStatusUpdateSerializer,
)

from django.db.models import Count, Sum
from rest_framework.permissions import IsAuthenticated


# ========== FOYDALANUVCHI API ==========
# Mahsulotlar ro‘yxati (faqat aktivlar)
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer


# Yangi buyurtma yaratish
class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()


# ========== ADMIN API ==========
# Mahsulotlar ro‘yxati (admin uchun)
class ProductAdminListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductAdminSerializer
    permission_classes = [IsAuthenticated]


class ProductAdminDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductAdminSerializer
    permission_classes = [IsAuthenticated]


# Buyurtmalar ro‘yxati (admin uchun)
class OrderAdminListView(generics.ListAPIView):
    queryset = Order.objects.all().order_by('-created_at')
    serializer_class = OrderAdminSerializer
    permission_classes = [IsAuthenticated]


# Buyurtma statusini o‘zgartirish (PATCH)
class OrderStatusUpdateView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderStatusUpdateSerializer
    permission_classes = [IsAuthenticated]


# Qidiruv: ism, telefon raqam, yoki buyurtma kodi bo‘yicha
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def order_search_view(request):
    query = request.GET.get('query', '')
    orders = Order.objects.filter(
        models.Q(customer_name__icontains=query) |
        models.Q(phone_number__icontains=query) |
        models.Q(order_code__icontains=query)
    )
    serializer = OrderAdminSerializer(orders, many=True)
    return Response(serializer.data)


# Statistik ma'lumotlar
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def statistics_view(request):
    orders = Order.objects.filter(status='done')
    total_income = 0
    for order in orders:
        product = order.product
        total_income += product.box_price if order.is_box and product.box_price else product.price

    stats = {
        'total_income': total_income,
        'total_orders': Order.objects.count(),
        'by_status': {
            'new': Order.objects.filter(status='new').count(),
            'confirmed': Order.objects.filter(status='confirmed').count(),
            'done': Order.objects.filter(status='done').count(),
            'archived': Order.objects.filter(status='archived').count(),
        },
        'top_products': Product.objects.annotate(
            order_count=Count('order')
        ).order_by('-order_count')[:5].values('name', 'order_count')
    }

    return Response(stats)
