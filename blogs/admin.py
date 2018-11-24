from django.contrib import admin

from blogs.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):

    fields = ['author', 'name', 'description']
    readonly_fields = ['id']
    list_display = ['name', 'description', 'author_fullname']
    search_fields = ['name', 'description']
    ordering = ['author']

    def author_fullname(self, obj):
        return '{0} {1}'.format(obj.author.first_name, obj.author.last_name)

    author_fullname.admin_order_field = 'author__first_name'

    def get_readonly_fields(self, request, obj=None):
        # author can't be modified (is readonly for update operations)
        if obj:
            return self.readonly_fields + ['author']
        return self.readonly_fields
