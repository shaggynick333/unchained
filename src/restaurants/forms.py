from django import forms
from django.db import models
from .models import RestaurantLocation
from .validators import validate_category

class RestaurantCreateForm(forms.Form):
    name = models.CharField()
    location = models.CharField()
    category = models.CharField()

    def clean_name(self):
        name = self.cleaned_data.get("name")
        if name == "Hello":
            raise forms.ValidationError("Not a valid name")
        return name

class RestaurantLocationCreateForm(forms.ModelForm):
    class Meta:
        model = RestaurantLocation
        fields = [
            'name',
            'location',
            'category',
            'slug'
        ]
