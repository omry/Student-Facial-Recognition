# Generated by Django 3.0.3 on 2020-03-04 21:44

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Recognition', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='image_features',
            field=jsonfield.fields.JSONField(default=None, null=True),
        ),
    ]
