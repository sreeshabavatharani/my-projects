# Generated by Django 4.2.10 on 2024-03-03 14:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Movie_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="movie_data",
            name="poster",
            field=models.ImageField(upload_to="Galary"),
        ),
    ]