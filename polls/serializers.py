# shop/serializers.py

from rest_framework import serializers
from .models import Product, Order

# Foydalanuvchi uchun mahsulotlarni ko‘rsatish
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'image',
            'description',
            'price',
            'box_price',
            'has_box',
            'box_count',
            'box_description',
        ]


# Admin uchun mahsulotlarni CRUD qilish serializer
class ProductAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


# Foydalanuvchi buyurtma beradi
class OrderCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['customer_name', 'phone_number', 'product', 'is_box']

    def create(self, validated_data):
        return Order.objects.create(**validated_data)


# Admin uchun buyurtmalarni ko‘rish va tahrirlash
class OrderAdminSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'order_code',
            'customer_name',
            'phone_number',
            'product',
            'is_box',
            'status',
            'created_at',
        ]


# Statusni alohida yangilash uchun serializer (PATCH uchun)
class OrderStatusUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['status']
