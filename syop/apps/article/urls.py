from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ArticleList, ArticleDetail

urlpatterns = [
    path('articles/', ArticleList.as_view()),
    path('article/<int:pk>/', ArticleDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
