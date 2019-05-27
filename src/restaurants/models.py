from django.db import models
from django.conf import settings
from django.urls import reverse
from django.db.models.signals import pre_save, post_save
from django.db.models import Q
from .utils import unique_slug_generator
from .validators import validate_category

User = settings.AUTH_USER_MODEL
# Create your models here.

class RestaurantLocationQuerySet(models.query.QuerySet):
    def search(self, query):
        if query:
            return self.filter(
                Q(name__icontains=query)|
                Q(location__icontains=query)|
                Q(category__icontains=query)
                ).distinct()
        return self

class RestaurantLocationManager(models.Manager):
    def get_queryset(self):
        return RestaurantLocationQuerySet(self.model, using=self._db)

    def search(self, query):
        return self.get_queryset().search(query)

class RestaurantLocation(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120, null=True, blank=True)
    category = models.CharField(max_length=120, null=True, blank=True, validators=[validate_category])
    slug = models.SlugField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    objects = RestaurantLocationManager()

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('restaurant-detail', kwargs={'slug': self.slug})

    @property
    def title(self):
        return str(self.name)

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    print('Saving...')
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=RestaurantLocation)
