from django.contrib import admin

from blogs.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    readonly_fields = ['owner', 'slug']
    list_display = ['name', 'description', 'owner_fullname']
    search_fields = ['name', 'description', 'slug']
    ordering = ['owner']

    def owner_fullname(self, obj):
        return '{0} {1}'.format(obj.owner.first_name, obj.owner.last_name)

    owner_fullname.admin_order_field = 'owner__first_name'
