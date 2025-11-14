from django.contrib import admin

from .models import Shoping,UserCreate,Product

admin.site.register(UserCreate)
admin.site.register(Product)
admin.site.register(Shoping)