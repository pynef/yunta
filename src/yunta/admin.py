from django.contrib import admin
from .models import (
    Usuario,
    Junta,
    Monedero
)

admin.site.register(Usuario)
admin.site.register(Junta)
admin.site.register(Monedero)
