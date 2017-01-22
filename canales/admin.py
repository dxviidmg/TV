from django.contrib import admin
from .models import *

class CanalAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('enlace', )}


admin.site.register(Canal, CanalAdmin)
admin.site.register(Categoria)