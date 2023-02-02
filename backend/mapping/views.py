import json
from django.http import JsonResponse

from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import api_view

from .models import SolarRoof
from .serializers import SolarRoofSerializer

import os
from django.conf import settings
import geojson


class RoofViewSet(viewsets.ModelViewSet):
    queryset = SolarRoof.objects.all()
    serializer_class = SolarRoofSerializer

@method_decorator(csrf_exempt, name='dispatch') # Allows cross-site requests
class Map(View):
    """ Retrieve the map in GeoJson form
    """
    def get(self, request):
 

        f = open(os.path.join(settings.BASE_DIR, 'penrith-wgs84.geojson'))

        # At this point, we could use the Python geojson package to read features into a featureCollection
        # featureCollection = geojson.load(f)
        # print(featureCollection)

        # Instead simply read the raw json and write out as a json response
        map_dict = json.load(f)

        return JsonResponse(map_dict)