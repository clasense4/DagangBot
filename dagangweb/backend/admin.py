from django.contrib import admin

# Register your models here.
from .models import User
from .models import Product
from .models import Cart
from .models import Payment
from .models import PaymentProduct

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'telegram_id', 'register_date')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'price', 'total_price')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'total', 'created_at', 'updated_at')

@admin.register(PaymentProduct)
class PaymentProductAdmin(admin.ModelAdmin):
    pass
    list_display = ('payment', 'product', 'quantity', 'sub_total', 'created_at')
