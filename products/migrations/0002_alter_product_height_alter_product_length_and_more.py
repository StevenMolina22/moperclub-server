# Generated by Django 5.0.2 on 2024-02-27 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='height',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='length',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='width',
            field=models.FloatField(null=True),
        ),
    ]
