from django.contrib import admin
from website.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'created_date', 'update_date')
    list_filter = ('created_date', 'update_date')
    date_hierarchy = 'created_date'
    search_fields = ['name', 'email', 'subject', 'message']
    list_per_page = 20
    ordering = ['created_date']
    empty_value_display = 'empty'


# Register your models here.
admin.site.register(Contact, ContactAdmin)
