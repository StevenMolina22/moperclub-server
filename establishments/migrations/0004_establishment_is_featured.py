# Generated by Django 4.1.3 on 2024-03-09 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('establishments', '0003_remove_establishment_is_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='establishment',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]
