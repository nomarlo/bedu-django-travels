from django.contrib import admin

# Register your models here.
from tours.models import User, Zone, Tour, Salida


class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "last_name", "email")


class TourAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id", "name", "slug", "type",
                    "description", "pais", "zonaSalida", "zonaLlegada")


class SalidaAdmin(admin.ModelAdmin):
    # Se sobre escribe lo que hace __str__
    list_display = ("id", "fechaInicio", "fechaFin", "asientos", "precio",
                    "tour")


admin.site.register(Salida, SalidaAdmin)

admin.site.register(User, UserAdmin)
admin.site.register(Zone)
admin.site.register(Tour, TourAdmin)
