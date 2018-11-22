from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_extensions.routers import NestedRouterMixin



from blogs.api import BlogsViewSet
from blogs.views import NewBlogView, BlogListView, UserBlogsView
from posts.api import PostsViewSet
from posts.views import BlogView

class NestedDefaultRouter(NestedRouterMixin, DefaultRouter):
    pass

router = NestedDefaultRouter()

blogs_router = router.register('blogs', BlogsViewSet)
blogs_router.register(
    'posts', PostsViewSet,
    base_name='blog-posts',
    parents_query_lookups=['blogs'])

#router.register('blogs', BlogsViewSet, base_name='blogs')

urlpatterns = [

    path('blogs/', BlogListView.as_view(), name='blogs'),
    path('blogs/new/', NewBlogView.as_view(), name='new-blog'),
    path('users/<slug:username>/blogs/', UserBlogsView.as_view(), name='user-blogs'),
    path('blogs/<slug:slug>/', BlogView.as_view(), name='blog'),


    # API
    path('api/1.0/', include(router.urls)),
    #path('api/1.0/blogs/<slug:username>', BlogPostsAPIView.as_view(), name='blog-posts-api'),

]
