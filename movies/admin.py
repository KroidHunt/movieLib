from dataclasses import fields
from django.contrib import admin
from .models import Movie, Crew


class CrewAdmin(admin.TabularInline):
    model = Crew


class MovieAdmin(admin.ModelAdmin):
    inline = [CrewAdmin]


admin.site.register(Movie, MovieAdmin)
admin.site.register(Crew)
