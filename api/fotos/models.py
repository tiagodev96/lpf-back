from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Ensaio(models.Model):
    nome = models.CharField(max_length=255)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        related_name="ensaios",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.nome


class Foto(models.Model):
    titulo = models.CharField(max_length=255)
    imagem = models.ImageField(upload_to="fotos/assets/")
    ensaio = models.ForeignKey(
        Ensaio, on_delete=models.CASCADE, related_name="fotos", null=True, blank=True
    )

    def __str__(self):
        return self.titulo
