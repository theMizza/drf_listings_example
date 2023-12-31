from rest_framework import serializers
from .models import Listings, Categories


class ListingsSerializer(serializers.ModelSerializer):
    """Listings model serializer"""
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())  # add user to listing

    class Meta:
        model = Listings
        fields = ('title', 'content', 'category', 'user')


class ListingCategoriesSerializer(serializers.ModelSerializer):
    """Categories model serializer"""
    class Meta:
        model = Categories
        fields = '__all__'
