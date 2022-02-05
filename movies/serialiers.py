from dataclasses import fields
from rest_framework import serializers
from .models import Movie, Crew


class MovieSerializer(serializers.ModelSerializer):
    cast = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = [
            'poster',
            'rating',
            'cast',
            'name',
            'description',
        ]

    def get_cast(self, obj):
        return "no one"


class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = '__all__'
