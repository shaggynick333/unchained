from django.urls import path, include, re_path

from .views import (
    ItemCreateView,
    ItemDetailView,
    ItemListView,
    ItemUpdateView
)

urlpatterns = [
    re_path(r'^create/$', ItemCreateView.as_view(), name='create'),
    re_path(r'^(?P<pk>\d+)/$', ItemUpdateView.as_view(), name='detail'),
    #re_path(r'^(?P<pk>\d+)/update/$', ItemUpdateView.as_view(), name='update'),
    re_path(r'^$', ItemListView.as_view(), name='list')
]
