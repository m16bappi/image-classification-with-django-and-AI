# Generated by Django 3.2 on 2021-04-14 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_imageextractor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageextractor',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]