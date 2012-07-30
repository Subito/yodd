from django.contrib import admin
from updater.models import Host, Update

class HostAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'last_updated', 'added',]

class UpdateAdmin(admin.ModelAdmin):
    list_display = ['__unicode__', 'from_ip', 'message',]

admin.site.register(Host, HostAdmin)
admin.site.register(Update, UpdateAdmin)
