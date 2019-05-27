from django.urls import path, include, re_path
from .views import ProfileDetailView

urlpatterns = [
    re_path(r"^(?P<username>[\w-]+)/$", ProfileDetailView.as_view(), name="detail")
    
]