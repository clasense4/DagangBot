from django.db import models


class User(models.Model):
    username = models.TextField(null=True)
    telegram_id = models.TextField(null=True)
    first_name = models.TextField(null=True)
    last_name = models.TextField(null=True)
    register_date = models.TextField(null=True)

class Product(models.Model):
    name = models.TextField(null=True)
    price = models.TextField(null=True)
