# Generated by Django 3.2.9 on 2022-04-03 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stories',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]