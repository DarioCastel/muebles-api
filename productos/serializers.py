from rest_framework import serializers
from productos.models import Producto, Categoria, ProductoImagen


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ["id", "nombre"]


class ProductoImagenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoImagen
        fields = ["url"]


class ProductoSerializer(serializers.ModelSerializer):
    categoria = serializers.CharField(source="categoria.nombre")
    imagenes = serializers.SerializerMethodField()
    medidas = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = [
            "id",
            "nombre",
            "slug",
            "categoria",
            "descripcion",
            "precio",
            "medidas",
            "peso_kg",
            "stock",
            "imagenes",
        ]

    def get_imagenes(self, obj):
        return [img.url for img in obj.imagenes.all()]

    def get_medidas(self, obj):
        return {
            "largo": obj.largo,
            "alto": obj.alto,
            "profundidad": obj.profundidad,
        }
