from rest_framework import serializers


# from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers

from .models import SolarRoof


class SolarRoofSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolarRoof
        fields = ['tooltip']
