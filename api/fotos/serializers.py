from rest_framework import serializers

from .models import Categoria, Ensaio, Foto


class FotoSerializer(serializers.ModelSerializer):
    ensaio_obj = serializers.SerializerMethodField()

    class Meta:
        model = Foto
        fields = ["id", "titulo", "imagem", "ensaio", "ensaio_obj"]

    def get_ensaio_obj(self, obj):
        return {
            "id": obj.ensaio.id if obj.ensaio else None,
            "nome": obj.ensaio.nome if obj.ensaio else None,
        }


class EnsaioSerializer(serializers.ModelSerializer):
    categoria_obj = serializers.SerializerMethodField()

    class Meta:
        model = Ensaio
        fields = ["id", "nome", "categoria", "categoria_obj"]

    def get_categoria_obj(self, obj):
        return {
            "id": obj.categoria.id if obj.categoria else None,
            "nome": obj.categoria.nome if obj.categoria else None,
        }


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = "__all__"
