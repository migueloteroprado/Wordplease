from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View

from posts.forms import NewPostForm
from posts.models import Post
from project.settings import ITEMS_PER_PAGE


class PostListView(View):

    def get(self, request):
        posts_list = Post.objects.prefetch_related('categories').select_related('owner').filter(published=True).order_by('-last_modification')
        paginator = Paginator(posts_list, ITEMS_PER_PAGE)
        page = request.GET.get('page')
        posts = paginator.get_page(page)
        context = {'posts': posts}
        return render(request, 'posts/home.html', context)


class NewPostView(View):

    @method_decorator(login_required)
    def get(self, request):
        form = NewPostForm()
        return render(request, 'posts/new-post.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        new_post = Post(owner=request.user)
        form = NewPostForm(request.POST, request.FILES, instance=new_post)
        if form.is_valid():
            new_post = form.save()
            messages.success(request, 'Post {0} created successfully!'.format(new_post.title))
            form = NewPostForm()
        return render(request, 'posts/new-post.html', {'form': form})
