# Generated by Django 3.1.3 on 2020-11-27 03:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_food_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
