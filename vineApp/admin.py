from django.contrib import admin

from vineApp.models import GrapeVarity, WineVarity, StoredBarrel


class GrapeVarityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'place', 'harvest_season')
    list_display_links = ('title', )
    list_editable = ('place',)
    fields = ('title', 'place', 'harvest_season')


class WineVarityAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'types_of_wine', 'grape_varity', 'color')
    list_display_links = ('title', )
    list_editable = ('grape_varity', 'color')
    fields = ('title', 'types_of_wine', 'grape_varity', 'color', 'aging_barrel', 'aging_bottel')


class StoredBarrelAdmin(admin.ModelAdmin):
    list_display = ('id', 'location', 'wine_varity', 'volume', 'date_of_manufacture', 'is_empty')
    list_display_links = ('location', )
    list_editable = ('wine_varity', 'volume')
    fields = ('location', 'wine_varity', 'volume', 'date_of_manufacture', 'is_empty')


admin.site.register(GrapeVarity, GrapeVarityAdmin)
admin.site.register(WineVarity, WineVarityAdmin)
admin.site.register(StoredBarrel, StoredBarrelAdmin)
