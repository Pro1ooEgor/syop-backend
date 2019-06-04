from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from comment.views import CommentList

urlpatterns = [
    path('comments/<int:title_pk>/', CommentList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
