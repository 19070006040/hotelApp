# Generated by Django 5.0.1 on 2024-01-08 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='title_description',
            field=models.CharField(max_length=1000, verbose_name='One title about the hotel'),
        ),
    ]
