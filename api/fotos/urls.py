from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CategoriaViewSet,
    EnsaiosPorCategoriaView,
    EnsaioViewSet,
    FotosPorEnsaioView,
    FotoViewSet,
)

router = DefaultRouter()
router.register(r"categorias", CategoriaViewSet)
router.register(r"ensaios", EnsaioViewSet)
router.register(r"fotos", FotoViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path(
        "ensaios/<int:ensaio_id>/fotos/",
        FotosPorEnsaioView.as_view(),
        name="fotos-por-ensaio",
    ),
    path(
        "categorias/<int:categoria_id>/ensaios/",
        EnsaiosPorCategoriaView.as_view(),
        name="ensaios-por-categoria",
    ),
]
