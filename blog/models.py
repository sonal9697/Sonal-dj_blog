from django.db import models
from django.utils import timezone
# to set author i.e user from user table
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

# creating post model-


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()  # no limitation of line use
    date_posted = models.DateTimeField(default=timezone.now)
    # need author having relation with users table in Django
    author = models.ForeignKey(User, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})


class morepost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()  # no limitation of line use
    date_posted = models.DateTimeField(default=timezone.now)
    # need author having relation with users table in Django
    author = models.ForeignKey(User, on_delete=models.CASCADE)
