from rest_framework.routers import DefaultRouter
from productos.views import ProductoViewSet, CategoriaViewSet

router = DefaultRouter()
router.register("productos", ProductoViewSet, basename="producto")
router.register("categorias", CategoriaViewSet, basename="categoria")

urlpatterns = router.urls
