import os
from django.db import models
from django.conf import settings


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=60, null=False, blank=False)
    image = models.ImageField(upload_to='media/blog/image/', null=True, blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    timestamp = models.TimeField(auto_now=True)
    visitor = models.SmallIntegerField()
    hastag = models.CharField(max_length=10, null=True, blank=True)
    takedown = models.BooleanField(default=False)
    uri_path = models.CharField(max_length=120, null=True, blank=True, default='')

    def save(self):
        self.uri_path = self.title.replace(' ', '-')
        try:
            old_file_path = self.image.path
            if os.path.exists(old_file_path):
                os.remove(old_file_path)
                base_name, ext = os.path.splitext(self.image.name)
                self.image.name = str(self.uri_path) + ext
        except:
            super().save()

    def setImage(self, image):
        try:
            old_file_path = self.image.path
            if os.path.exists(old_file_path):
                os.remove(old_file_path)
        except:
            pass
        self.image = image
        base_name, ext = os.path.splitext(self.image.name)
        self.image.name = str(self.uri_path) + ext

    def __str__(self):
        return self.title


class Comment(models.Model):
    commented_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.CharField(max_length=160, null=False, blank=False)

    def __str__(self):
        return self.user