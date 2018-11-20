from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from blogs.models import Blog
from project.settings import ITEMS_PER_PAGE


class BlogListView(View):

    def get(self, request):

        blog_list = Blog.objects.all().select_related('owner').order_by('name')

        # Pagination
        paginator = Paginator(blog_list, ITEMS_PER_PAGE)
        page = request.GET.get('page')
        blogs = paginator.get_page(page)

        return render(request, 'blogs/blogs.html', {'blogs': blogs})