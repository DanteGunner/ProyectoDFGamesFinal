from django.contrib import admin
from .models import Compania, Juego

# Register your models here.

class JuegoAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'compania', 'anio_lanzamiento')
    search_fields = ['codigo', 'nombre']
    list_filter = ('compania',)

admin.site.register(Compania)
admin.site.register(Juego, JuegoAdmin)
