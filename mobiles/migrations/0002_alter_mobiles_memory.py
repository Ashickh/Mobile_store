# Generated by Django 4.0.4 on 2022-06-13 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobiles',
            name='memory',
            field=models.TextField(max_length=50),
        ),
    ]
