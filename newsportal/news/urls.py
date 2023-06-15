from django.urls import path
from .views import (PostsList, PostDetail, SearchPost, PostCreate, PostUpdate, PostDelete,
                    ArticleCreate, ArticleUpdate, ArticleDelete)

urlpatterns = [
    path('search/', SearchPost.as_view(), name='search_post'),
    path('', PostsList.as_view(), name='post_list'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('article/create/', ArticleCreate.as_view(), name='article_create'),
    path('article/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_update'),
    path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='post_list'),
]
