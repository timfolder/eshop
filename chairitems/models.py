from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Chair(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=3, max_digits=4)
    description = models.TextField(max_length=251)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="chairs")
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("chair_details", args=[self.slug])
    

    def __str__(self) -> str:
        return self.title + " " + self.owner.username
# Create your models here.
