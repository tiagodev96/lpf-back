from django.contrib import admin

from .models import Categoria, Ensaio, Foto

admin.site.register(Categoria)
admin.site.register(Foto)
admin.site.register(Ensaio)
