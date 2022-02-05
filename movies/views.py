from pyexpat import model
from rest_framework import viewsets

from movies.serialiers import MovieSerializer
from .models import Movie, Crew


class MovieViewSet(viewsets.ModelViewSet):
    model = Movie
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class CrewViewSet(viewsets.ModelViewSet):
    model = Crew
    serializer_class = MovieSerializer
    queryset = Crew.objects.all()
