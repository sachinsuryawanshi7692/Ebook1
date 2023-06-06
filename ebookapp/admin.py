from django.contrib import admin
from ebookapp.models import Product

# Register your models here.

#admin.site.register(Products)

#Difine ModelAdminClass

class ProductAdminClass(admin.ModelAdmin):
    list_display=['name','cat','price','date','status','eimage']
    list_filter=['status','cat']

admin.site.register(Product,ProductAdminClass)
admin.site.site_header="E-Bookshop (Admin Panel)"




     
