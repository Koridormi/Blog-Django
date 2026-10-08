from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.PROTECT,
        related_name = 'posts'
    )

    def __str__(self):
        return self.title