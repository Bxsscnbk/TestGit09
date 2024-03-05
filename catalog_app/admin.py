from django.contrib import admin

# Register your models here.
from .models import MyUser, Product

# Register your models here.
admin.site.register(MyUser)
admin.site.register(Product)