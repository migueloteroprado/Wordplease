from django.contrib import admin
from django.utils.safestring import mark_safe

from blogs.models import Blog
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    #readonly_fields = ['author', 'blog']
    list_display = ['title', 'image_tag', 'author_fullname', 'formatted_pub_date']
    search_fields = ['title', 'summary', 'body']
    list_filter = ['categories']
    ordering = ['author']

    def author_fullname(self, obj):
        return '{0} {1}'.format(obj.author.first_name, obj.author.last_name)

    def image_tag(self, obj):
        return mark_safe('<img src="{0}" alt="{1}" title="{1}" width="auto" height="80">'.format(obj.image.url, obj.title)) \
            if obj.image\
            else '-'

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "blog":
            kwargs["queryset"] = Blog.objects.filter(author=self)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


    image_tag.short_description = 'Image'

    author_fullname.admin_order_field = 'author__first_name'

    def formatted_pub_date(self, obj):
        return obj.pub_date.strftime('%d/%m/%Y %H:%M')

    formatted_pub_date.short_description = 'Pub date'
    formatted_pub_date.admin_order_field = 'pub_date'
