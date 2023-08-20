from django.db import models


class EmailSubscribe(models.Model):
    email = models.EmailField()
