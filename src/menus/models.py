from django.conf import settings
from django.db import models
from restaurants.models import RestaurantLocation
from django.urls import reverse
# Create your models here.
class Item(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(RestaurantLocation, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    contents = models.TextField(help_text='Separate each item by comma')
    excludes = models.TextField(blank=True, null=True)
    public = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('menus:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-updated', '-timestamp']

    def get_contents(self):
        return self.contents.split(",")
 
    def get_excludes(self):
        return self.excludes.split(",")