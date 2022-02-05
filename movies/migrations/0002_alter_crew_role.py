# Generated by Django 4.0.1 on 2022-01-31 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crew',
            name='role',
            field=models.FloatField(choices=[('protagonist', 'protagonist'), ('antagonist', 'antagonist'), ('director', 'director'), ('assistant director', 'assistant director'), ('producer', 'producer'), ('assistant producer', 'assistant producer'), ('actress', 'actress'), ('heroine', 'heroine'), ('hero', 'hero'), ('actor', 'actor')], default='protagonist'),
        ),
    ]
