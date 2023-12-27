from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    body = models.TextField()
    slug = models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('body', )

    def __str__(self):
        return f'{self.slug} - {self.body}'

    def get_absolute_url(self):
        return reverse('home:post_detail', args=[self.id, self.slug])