from django.db import models


class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    article = models.ForeignKey('article.Article', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('user.Author', on_delete=models.CASCADE, related_name='comments')
