from django.contrib import admin
from .models import Categoria, Producto, ProductoImagen, Combo

admin.site.register(Categoria)
admin.site.register(Producto)
admin.site.register(ProductoImagen)
admin.site.register(Combo)
