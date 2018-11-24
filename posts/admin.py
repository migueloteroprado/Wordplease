from django.contrib import admin
from django import forms
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe

from posts.models import Post


class PostAdminForm(forms.ModelForm):

    def clean_blog(self):
        # check if author and blog's author are the same
        if self.cleaned_data.get('author') == self.cleaned_data.get('blog').author:
            return self.cleaned_data.get('blog')
        raise ValidationError('Post author and blog author must be the same')

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    form = PostAdminForm
    list_display = ['title', 'image_tag', 'pub_date', 'author_fullname', 'blog_name']
    search_fields = ['title', 'summary', 'body']
    list_filter = ['categories']
    ordering = ['author', 'pub_date']
    readonly_fields = ['creation_date', 'last_modification']

    def author_fullname(self, obj):
        return '{0} {1}'.format(obj.author.first_name, obj.author.last_name)

    def blog_name(self, obj):
        return obj.blog.name

    def image_tag(self, obj):
        return \
            mark_safe('<img src="{0}" alt="{1}" title="{1}" width="auto" height="80">'.format(obj.image.url, obj.title)) \
            if obj.image else '-'

    image_tag.short_description = 'Image'

    author_fullname.admin_order_field = 'author__first_name'

    fieldsets = [
        [None, {
            'fields': ['author', 'blog', 'title']
        }],
        ['Media', {
            'fields': ['image', 'video']
        }],
        ['Detail', {
            'fields': ['summary', 'body', 'categories'],
        }],
        ['Dates', {
            'fields': ['pub_date', 'creation_date', 'last_modification']
        }]
    ]

    def get_readonly_fields(self, request, obj=None):
        # author and blog can't be modified (it's readonly for update operations)
        if obj:
            return self.readonly_fields + ['author', 'blog']
        return self.readonly_fields


