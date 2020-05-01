from django.contrib import admin
from .models import Lista


class ListaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name_lista')
    list_display_links = ('id', 'name_lista')
    filter_horizontal = ('produtos',)


admin.site.register(Lista, ListaAdmin)
# TODO: entender isso
