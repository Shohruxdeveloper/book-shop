from django.contrib import admin
from .models import Books, Category, Cart, User

admin.site.register(Category)
admin.site.register(Books)
admin.site.register(Cart)
admin.site.register(User)
