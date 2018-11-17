from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from posts.models import Post


class PostListView(View):

    def get(self, request):
        # 1) Obtener los posts de la base de datos que están publicados
        posts_list = Post.objects.prefetch_related('categories').select_related('owner').filter(published=True).order_by('-last_modification')

        paginator = Paginator(posts_list, 10)  # Show 10 posts per page
        page = request.GET.get('page')
        posts = paginator.get_page(page)

        # 2) Pasar los anuncios a la plantilla para que ésta los muestre en HTML
        context = {'posts': posts}
        return render(request, 'posts/home.html', context)
