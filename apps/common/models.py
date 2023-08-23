from django.db import models
from ckeditor.fields import RichTextField


class EmailSubscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Article(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images_of_article/")
    is_prime = models.BooleanField(default=False)
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
