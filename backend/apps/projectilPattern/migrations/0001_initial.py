# Generated by Django 3.0.8 on 2020-07-09 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectilPattern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('interval', models.DurationField()),
                ('spreadAngle', models.DecimalField(decimal_places=10, max_digits=12)),
                ('range', models.DecimalField(decimal_places=10, max_digits=12)),
            ],
        ),
    ]
