from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=150)
    text = models.TextField()
    html = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('user.Author', on_delete=models.CASCADE, related_name='articles')
