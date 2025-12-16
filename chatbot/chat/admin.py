from django.contrib import admin
from .models import Chat
from import_export.admin import ExportMixin


@admin.register(Chat)
class ChatAdmin(ExportMixin, admin.ModelAdmin):
  pass