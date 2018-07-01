from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=55)
    description = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete = models.CASCADE, default=None, related_name="blogs")

    def __str__(self):
        return self.title

    def summary(self):
        return self.description[:100]

class Post(models.Model):
    title = models.CharField(max_length=55)
    content = models.TextField()
    published = models.DateTimeField()
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE, related_name="posts")


    def __str__(self):
        return self.title


    def summary(self):
        return self.content[:200]

