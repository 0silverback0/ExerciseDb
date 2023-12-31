from django.urls import path
from .views import CreateArticleView, ArticleListView, ArticleUpdateAPIView, SearchArticlesView, ArticleDetailView, ArticleDeleteAPIView

urlpatterns = [
     path('', ArticleListView.as_view(), name='list-article'),
     path('create/', CreateArticleView.as_view(), name='create-article'),
     path('edit/<int:pk>/', ArticleUpdateAPIView.as_view(), name='edit-article'),
     path('article/<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
     path('search/', SearchArticlesView.as_view(), name='article_search'),
     path('<int:pk>/delete/', ArticleDeleteAPIView.as_view(), name='article-delete'),
]