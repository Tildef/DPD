from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class post(models.Model):
    titel=models.CharField(max_length=100)
    innehall=models.TextField()
    datum_skapad=models.DateTimeField(default=timezone.now)
    forfattare=models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.titel

    def get_absolute_url(self):
        return reverse('post-sida', kwargs={'pk':self.pk})