# Generated by Django 3.0.3 on 2020-02-08 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Recognition', '0002_auto_20200208_1255'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='semester',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='students',
            name='year',
            field=models.IntegerField(default=1),
        ),
        migrations.CreateModel(
            name='Units',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_title', models.CharField(max_length=50)),
                ('unit_code', models.CharField(max_length=30, unique=True)),
                ('year', models.IntegerField()),
                ('semester', models.IntegerField()),
                ('unit_lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unit_lecturer', to='Recognition.Lecturer')),
            ],
        ),
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_attended', models.BooleanField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_bookings', to='Recognition.Students')),
                ('unit_booked', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Recognition.Units')),
            ],
        ),
    ]
