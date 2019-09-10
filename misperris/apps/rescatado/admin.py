from django.contrib import admin
from apps.rescatado.models import Estado, Raza, Rescatado

# Register your models here.

admin.site.register(Raza)
admin.site.register(Estado)
admin.site.register(Rescatado)