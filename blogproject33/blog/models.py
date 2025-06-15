from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)       # for blog title
    content = models.TextField()                   # for blog content
    created_at = models.DateTimeField(auto_now_add=True)  # timestamp

    def __str__(self):
        return self.title  # shows title in admin panel


# Create your models here.
