from django.contrib import admin

from Biblioteca.models import Autor
from Biblioteca.models import Libro
from Biblioteca.models import Ejemplar
from Biblioteca.models import Usuario


class UsuarioAdmin(admin.ModelAdmin):
	list_display = ('Nombre', 'Direccion','Telefono')
	fieldsets = (
		('Datos', {
			'fields': ('Nombre',)
			}),
		('Contacto',{
			'fields': ('Direccion', 'Telefono')
			})
	)

class LibroAdmin(admin.ModelAdmin):
    list_display = ('Titulo', 'Editorial')




class EjemplarAdmin(admin.ModelAdmin):
	list_display = ('Libro', 'Usuario','Localizacion')
	list_filter = ('Libro',)	




class LibroInline(admin.TabularInline):
    model = Libro




class AutorAdmin(admin.ModelAdmin):
	list_display = ('Nombre',)
	inlines = [LibroInline, ]
	search_fields = ['Nombre', ]






# Register your models here.
admin.site.register(Autor,AutorAdmin)
admin.site.register(Libro,LibroAdmin)
admin.site.register(Ejemplar, EjemplarAdmin)
admin.site.register(Usuario, UsuarioAdmin)
