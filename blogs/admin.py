from django.contrib import admin

from blogs.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    readonly_fields = ['slug']
    list_display = ['name', 'description', 'author_fullname']
    search_fields = ['name', 'description']
    ordering = ['author']

    def author_fullname(self, obj):
        return '{0} {1}'.format(obj.author.first_name, obj.author.last_name)

    author_fullname.admin_order_field = 'author__first_name'
