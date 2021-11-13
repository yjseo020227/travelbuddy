# Generated by Django 3.2.9 on 2021-11-13 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recommendations', '0003_places_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='places',
            name='location',
            field=models.CharField(default='Seoul', max_length=30),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Foot_Traffic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('traffic_level', models.FloatField()),
                ('date', models.DateField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recommendations.places')),
            ],
        ),
    ]
