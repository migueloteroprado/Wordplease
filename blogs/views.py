from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views import View

from blogs.forms import BlogForm
from blogs.models import Blog
from posts.models import Post
from project.settings import ITEMS_PER_PAGE


class BlogListView(View):

    def get(self, request):

        blog_list = Blog.objects.all().select_related('author').order_by('name')

        # Pagination
        paginator = Paginator(blog_list, ITEMS_PER_PAGE)
        page = request.GET.get('page')
        blogs = paginator.get_page(page)

        return render(request, 'blogs/blogs.html', {'blogs': blogs})


class UserBlogsView(View):

    def get(self, request, username):

        user = get_object_or_404(User, username=username)
        blog_list = Blog.objects.filter(author=user).select_related('author').order_by('name')

        # Pagination
        paginator = Paginator(blog_list, ITEMS_PER_PAGE)
        page = request.GET.get('page')
        blogs = paginator.get_page(page)

        return render(request, 'blogs/blogs.html', {'blogs': blogs})


class BlogView(View):

    def get(self, request, slug):

        blog = get_object_or_404(Blog, slug=slug)

        # if user is the blog propietary show all posts, otherwise show only published
        if request.user == blog.author:
            posts_list = Post.objects.select_related('author')\
                .filter(blog=blog.id).order_by('-pub_date')
        else:
            posts_list = Post.objects.select_related('author')\
                .filter(status=Post.PUBLISHED, blog=blog.id).order_by('-pub_date')

        paginator = Paginator(posts_list, ITEMS_PER_PAGE)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        context = {
            'posts': posts,
            'title': '{0} ({1} {2})'.format(blog.name, blog.author.first_name, blog.author.last_name)
        }
        return render(request, 'posts/posts.html', context)


class NewBlogView(View):

    @method_decorator(login_required)
    def get(self, request):
        form = BlogForm()
        return render(request, 'blogs/new-blog.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        new_blog = Blog(author=request.user)
        form = BlogForm(request.POST, instance=new_blog)

        if form.is_valid():
            new_blog = form.save()
            messages.success(request, 'Blog {0} created successfully!'.format(new_blog.name))
            form = BlogForm()

        return render(request, 'blogs/new-blog.html', {'form': form})
