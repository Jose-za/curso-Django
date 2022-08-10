from django.contrib import admin

from .models import Cursos

# Register your models here.
class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'update')
    list_display = ('nombre', 'curso', 'email','tiempo','fecha')
    search_fields = ('nombre', 'curso', 'email','tiempo', 'fecha')
    date_hierarchy = 'created'
    list_filter = ('curso','nombre', 'fecha')

admin.site.register(Cursos, AdministrarModelo)