from django.db import models
from django.contrib.auth.models import User


class Crew(models.Model):
    ROLE_CHOICES = [
        ("protagonist", "protagonist"),
        ("antagonist", "antagonist"),
        ("director", "director"),
        ("assistant director", "assistant director"),
        ("producer", "producer"),
        ("assistant producer", "assistant producer"),
        ("actress", "actress"),
        ("heroine", "heroine"),
        ("hero", "hero"),
        ("actor", "actor"),
    ]

    first_name = models.CharField(max_length=200, null=False, blank=False)
    last_name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to="uploads/artist/", blank=True)
    role = models.CharField(choices=ROLE_CHOICES,
                            default=ROLE_CHOICES[0][0], max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.first_name


class Movie(models.Model):
    RATING_CHOICES = [
        (1, 1),
        (1.5, 1.5),
        (2, 2),
        (2.5, 2.5),
        (3, 3),
        (3.5, 3.5),
        (4, 4),
        (4.5, 4.5),
        (5, 5),
    ]

    poster = models.ImageField(upload_to="uploads/movie/", blank=True)
    rating = models.FloatField(choices=RATING_CHOICES, default=1)
    cast = models.ManyToManyField(Crew)
    name = models.CharField(max_length=700)
    description = models.TextField()

    def __str__(self):
        return self.name
