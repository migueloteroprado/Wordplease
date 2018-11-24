from django.contrib import admin

from categories.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    fields = ['id', 'name', 'description']
    readonly_fields = ['id']
    list_display = ['name', 'description']
    search_fields = ['name', 'description']
    ordering = ['name']
