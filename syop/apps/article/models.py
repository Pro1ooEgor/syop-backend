from django.db import models


class Article(models.Model):
    name = models.CharField(max_length=150)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey()
