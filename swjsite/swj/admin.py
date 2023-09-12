from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemeberAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['name', 'body']
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
