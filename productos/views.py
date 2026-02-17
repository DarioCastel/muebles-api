from rest_framework.viewsets import ReadOnlyModelViewSet
from productos.models import Producto, Categoria
from productos.serializers import ProductoSerializer, CategoriaSerializer


class ProductoViewSet(ReadOnlyModelViewSet):
    serializer_class = ProductoSerializer

    def get_queryset(self):
        queryset = Producto.objects.all().prefetch_related("imagenes")

        categoria = self.request.query_params.get("categoria")
        if categoria:
            queryset = queryset.filter(categoria__id=categoria)

        return queryset


class CategoriaViewSet(ReadOnlyModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
