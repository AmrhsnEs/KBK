# Generated by Django 5.0.6 on 2024-06-30 18:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("reservations", "0006_review"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="edit_count",
            field=models.IntegerField(default=0),
        ),
    ]
