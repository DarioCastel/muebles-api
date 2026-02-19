from django.contrib import admin
from .models import Producto, ProductoImagen, Categoria, Combo


class ProductoImagenInline(admin.TabularInline):
    model = ProductoImagen
    extra = 1


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    inlines = [ProductoImagenInline]
    list_display = ("nombre", "categoria", "precio", "stock")
    prepopulated_fields = {"slug": ("nombre",)}


admin.site.register(Categoria)
admin.site.register(Combo)
