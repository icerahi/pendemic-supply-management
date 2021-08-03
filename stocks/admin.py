from django.contrib import admin
from .models import Stock, Request
# Register your models here.


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'equipment', 'message', 'created', 'accepted')
    list_display_links = ('user', 'equipment', 'message',
                          'created', 'accepted')
    search_fields = ('user,equipment', 'message')


@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'image', 'quantity', 'created')


admin.site.site_header = "Pendemic Supply Management"
admin.site.site_title = "Pendemic Supply Management"
admin.site.index_title = "Pendemic Supply Management"
