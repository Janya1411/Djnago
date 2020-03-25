from django.contrib import admin

from .models import NGO
from import_export.admin import ImportExportActionModelAdmin

@admin.register(NGO)


class ViewAdmin(ImportExportActionModelAdmin):
    pass