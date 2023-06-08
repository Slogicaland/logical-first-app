from django.contrib import admin
from .models import logical


@admin.register(logical)
class logicalAdmin(admin.ModelAdmin):
    pass
