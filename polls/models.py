# shop/models.py
from django.db import models
from django.utils.crypto import get_random_string

# Mahsulot modeli
class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.URLField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    box_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    has_box = models.BooleanField(default=False)
    box_count = models.PositiveIntegerField(default=0)
    box_description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name


# Buyurtma modeli
class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'Yangi'),
        ('confirmed', 'Tasdiqlangan'),
        ('done', 'Bajarilgan'),
        ('archived', 'Arxiv'),
    ]

    order_code = models.CharField(max_length=10, unique=True, blank=True)
    customer_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    is_box = models.BooleanField(default=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.order_code:
            self.order_code = self.generate_order_code()
        super().save(*args, **kwargs)

    def generate_order_code(self):
        return "B" + get_random_string(5).upper()

    def __str__(self):
        return f"{self.order_code} - {self.customer_name}"
