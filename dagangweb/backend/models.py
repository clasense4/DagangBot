from django.db import models


class User(models.Model):
    username = models.TextField(null=True)
    telegram_id = models.TextField(null=True)
    first_name = models.TextField(null=True)
    last_name = models.TextField(null=True)
    register_date = models.DateTimeField(null=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Product(models.Model):
    name = models.TextField(null=True)
    price = models.BigIntegerField(null=False)

    def __str__(self):
        return '%s' % (self.name)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return '%s %s, %s : %s' % (self.user.first_name, self.user.last_name, self.product.name, self.quantity)

    def price(self):
        return '%s' % (self.product.price)

    def total_price(self):
        return '%s' % (int(self.product.price) * int(self.quantity))