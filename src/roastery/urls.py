"""roastery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
from profiles.views import ProfileFollowToggle
from restaurants.views import (
RestaurantListView,
RestaurantDetailView,
RestaurantCreateView,
RestaurantUpdateView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^login/$', LoginView.as_view(), name='login'),
    re_path(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    re_path(r'^restaurants/$', RestaurantListView.as_view(), name='restaurants'),
    re_path(r'^restaurants/create/$', RestaurantCreateView.as_view(), name='restaurant-create'),
    re_path(r'^items/', include(('menus.urls', 'menus'), namespace='menus')),
    re_path(r'^restaurants/(?P<slug>[\w-]+)/$', RestaurantUpdateView.as_view(), name='restaurant-detail'),
    re_path(r'^u/', include(('profiles.urls', 'profiles'), namespace='profiles')),
    re_path(r'^about/$', TemplateView.as_view(template_name='about.html'), name='about'),
    re_path(r'^contact/$', TemplateView.as_view(template_name='contact.html'), name='contact'),
    re_path(r'^profile-follow/$', ProfileFollowToggle.as_view(), name='follow')
]
