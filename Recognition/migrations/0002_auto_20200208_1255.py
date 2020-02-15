# Generated by Django 3.0.3 on 2020-02-08 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Recognition', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='image',
            field=models.FileField(default=None, upload_to=''),
        ),
        migrations.AlterField(
            model_name='students',
            name='image_features',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
