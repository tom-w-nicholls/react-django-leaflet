from django.urls import include, path
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register('roofs', views.RoofViewSet)

# Wire up our API using automatic URL routing.

urlpatterns = [
    # ...
    path('', include(router.urls)),
]