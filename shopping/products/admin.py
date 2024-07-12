from django.contrib import admin
from . models import products,category,cart,cartitem,checkout


# Register your models here.
admin.site.register(products)
admin.site.register(category)
admin.site.register(cart)
admin.site.register(cartitem)
admin.site.register(checkout)

