from rest_framework import serializers
from .models import City, Mall, Shop

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']

class MallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mall
        fields = ['id', 'name']

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id', 'name', 'icon_image', 'x', 'y']
