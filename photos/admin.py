from django.contrib import admin
from django.utils.safestring import mark_safe

from photos.models import Photo

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner_name', 'license', 'visibility',)  # Campos del listado
    list_filter = ('license', 'visibility',)                         # Campos de filtrado
    search_fields = ('name', 'description',)                         # Campos de búsqueda
    readonly_fields = ('image_tag',)

    fieldsets = (
        ("Name and description", {
          'fields': ('name',),
        }),
        ('Author', {
            'fields': ('owner',),
        }),
        ('URL', {
            'fields': ('url','image_tag',),
            'classes': ('wide',),
        }),
        ('License and visibility', {
            'fields': ('license', 'visibility',),
            'classes': ('wide', 'collapse'),
        })
    )

    def owner_name(self, photo):
        return "{0} {1}".format(photo.owner.first_name, photo.owner.last_name)

    def image_tag(self, photo):
        return mark_safe("<img src={0}>".format(photo.url))

    owner_name.admin_order_field = "owner"
    owner_name.short_description = 'Propietario'


admin.site.register(Photo, PhotoAdmin)
