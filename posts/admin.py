import datetime
from django.contrib import admin
from django.utils.safestring import mark_safe

from blogs.models import Blog
from posts.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    #readonly_fields = ['author', 'blog']
    list_display = ['title', 'image_tag', 'author_fullname', 'pub_date']
    search_fields = ['title', 'summary', 'body']
    list_filter = ['categories', 'status']
    ordering = ['author']
    #readonly_fields = ['author']
    readonly_fields = ['pub_date', 'last_modification']

    def author_fullname(self, obj):
        return '{0} {1}'.format(obj.author.first_name, obj.author.last_name)

    def image_tag(self, obj):
        return mark_safe('<img src="{0}" alt="{1}" title="{1}" width="auto" height="80">'.format(obj.image.url, obj.title)) \
            if obj.image\
            else '-'

    image_tag.short_description = 'Image'

    author_fullname.admin_order_field = 'author__first_name'

    fieldsets = [
        [None, {
            'fields': ['title', 'author', 'blog', 'image', 'summary', 'status']
        }],
        ['Detail', {
            'fields': ['body', 'categories'],
        }],
        ['Important dates', {
            'fields': ['pub_date', 'last_modification']
        }]
    ]

    def save_model(self, request, obj, form, change):
        obj.pub_date = datetime.datetime.now() if obj.status == Post.PUBLISHED else None
        super(PostAdmin, self).save_model(request, obj, form, change)
