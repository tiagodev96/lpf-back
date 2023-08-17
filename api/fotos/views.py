from rest_framework import generics, viewsets

from .models import Categoria, Ensaio, Foto
from .serializers import CategoriaSerializer, EnsaioSerializer, FotoSerializer


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class EnsaiosPorCategoriaView(generics.ListAPIView):
    serializer_class = EnsaioSerializer

    def get_queryset(self):
        categoria_id = self.kwargs["categoria_id"]
        return Ensaio.objects.filter(categoria__id=categoria_id)


class EnsaioViewSet(viewsets.ModelViewSet):
    queryset = Ensaio.objects.all()
    serializer_class = EnsaioSerializer


class FotoViewSet(viewsets.ModelViewSet):
    queryset = Foto.objects.all()
    serializer_class = FotoSerializer


class FotosPorEnsaioView(generics.ListAPIView):
    serializer_class = FotoSerializer

    def get_queryset(self):
        ensaio_id = self.kwargs["ensaio_id"]
        return Foto.objects.filter(ensaio__id=ensaio_id)
