from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import filters
from django.http import JsonResponse
from django.views import View

# class CreateArticleView(generics.CreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer 

# class ArticleListView(generics.ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

# class ArticleUpdateAPIView(generics.UpdateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
    

# class ArticleDetailView(APIView):
#     def get(self, request, id, format=None):
#         try:
#             article = Article.objects.get(id=id)
#             serializer = ArticleSerializer(article)
#             return Response(serializer.data)
#         except Article.DoesNotExist:
#             return Response({'error': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)
        
# class SearchArticlesView(View):
#     def get(self, request):
#         # Get the search term from the query parameters
#         search_term = request.GET.get('title', '')

#         # Filter articles based on the search term
#         articles = Article.objects.filter(title__icontains=search_term)

#         # Check if any articles were found
#         if articles.exists():
#             # Serialize the articles or perform any other processing
#             serialized_articles = [{'id': article.id, 'title': article.title} for article in articles]

#             # Return the serialized articles as JSON response
#             return JsonResponse({'articles': serialized_articles})
#         else:
#             # Return an empty list if no articles match the search term
#             return JsonResponse({'articles': []})

from .permissions import IsSuperUserOrReadOnly

class CreateArticleView(generics.CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsSuperUserOrReadOnly]

class ArticleListView(generics.ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsSuperUserOrReadOnly]

class ArticleUpdateAPIView(generics.UpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsSuperUserOrReadOnly]

class ArticleDetailView(APIView):
    permission_classes = [IsSuperUserOrReadOnly]

    def get(self, request, id, format=None):
        try:
            article = Article.objects.get(id=id)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)
        except Article.DoesNotExist:
            return Response({'error': 'Article not found'}, status=status.HTTP_404_NOT_FOUND)
        
class SearchArticlesView(View):
    permission_classes = [IsSuperUserOrReadOnly]

    def get(self, request):
        # Get the search term from the query parameters
        search_term = request.GET.get('title', '')

        # Filter articles based on the search term
        articles = Article.objects.filter(title__icontains=search_term)

        # Check if any articles were found
        if articles.exists():
            # Serialize the articles or perform any other processing
            serialized_articles = [{'id': article.id, 'title': article.title} for article in articles]

            # Return the serialized articles as JSON response
            return JsonResponse({'articles': serialized_articles})
        else:
            # Return an empty list if no articles match the search term
            return JsonResponse({'articles': []})
