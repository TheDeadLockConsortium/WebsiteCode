from django.contrib import admin

from .models import Partner

class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'size', 'url')

    search_fields =('name', 'url')

    list_display_links = ('name')

admin.site.register(Partner, PartnerAdmin)