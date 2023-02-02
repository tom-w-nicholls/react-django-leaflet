# from mapping.views import char_count
from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from mapping import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include('mapping.urls')),
    path("map/", views.Map.as_view())
]
