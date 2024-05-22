from django.contrib import admin
from blog.models import Post


class Postadmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'status', 'created_date', 'published_date')
    list_filter = ('title', 'created_date', 'published_date')
    ordering = ['created_date']
    search_fields = ['title', 'content']
    readonly_fields = ('counted_view',)


# Register your models here.
admin.site.register(Post, Postadmin)
