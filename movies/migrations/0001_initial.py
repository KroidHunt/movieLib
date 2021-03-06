# Generated by Django 4.0.1 on 2022-01-31 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('picture', models.ImageField(blank=True, upload_to='uploads/artist/')),
                ('role', models.FloatField(choices=[('protagonist', 'protagonist'), ('antagonist', 'antagonist'), ('director', 'director'), ('assistant director', 'assistant director'), ('producer', 'producer'), ('assistant producer', 'assistant producer'), ('actress', 'actress'), ('heroine', 'heroine'), ('hero', 'hero'), ('actor', 'actor')], default=1)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster', models.ImageField(blank=True, upload_to='uploads/movie/')),
                ('rating', models.FloatField(choices=[(1, 1), (1.5, 1.5), (2, 2), (2.5, 2.5), (3, 3), (3.5, 3.5), (4, 4), (4.5, 4.5), (5, 5)], default=1)),
                ('name', models.CharField(max_length=700)),
                ('description', models.TextField()),
                ('cast', models.ManyToManyField(to='movies.Crew')),
            ],
        ),
    ]
