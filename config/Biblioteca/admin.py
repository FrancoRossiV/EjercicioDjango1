from django.contrib import admin

from Biblioteca.models import Autor
from Biblioteca.models import Libro
from Biblioteca.models import Ejemplar
from Biblioteca.models import Usuario

# Register your models here.
admin.site.register(Autor,)
admin.site.register(Libro,)
admin.site.register(Ejemplar,)
admin.site.register(Usuario,)
