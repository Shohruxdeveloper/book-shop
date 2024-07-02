from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    USER_ROLE_CHOICES = (
        ('admin', 'admin'),
        ('seller', 'seller'),
        ('user', 'user'),
    )

    phone_number = models.CharField(max_length=13, blank=True, null=True)
    image = models.ImageField(upload_to='user/', null=True, blank=True, default='user/img.png')
    address = models.CharField(max_length=100, null=True, blank=True)
    user_role = models.CharField(max_length=10, choices=USER_ROLE_CHOICES, default='user')

    def __str__(self):
        return self.username


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

    def str(self):
        return self.store_name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Category")

    def __str__(self):
        return self.name


class Books(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField()
    description = models.TextField()
    stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    @property
    def total_price(self):
        return self.price * self.quantity


class Cart(models.Model):
    books = models.OneToOneField(Books, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.books.name

