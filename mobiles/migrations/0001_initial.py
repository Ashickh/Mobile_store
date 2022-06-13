# Generated by Django 4.0.4 on 2022-06-13 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mobiles',
            fields=[
                ('mob_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('mob_name', models.CharField(max_length=120)),
                ('brand', models.CharField(max_length=120)),
                ('price', models.PositiveIntegerField(max_length=120)),
                ('color', models.CharField(max_length=120)),
                ('memory', models.PositiveIntegerField(max_length=50)),
            ],
        ),
    ]
