# Generated by Django 4.2 on 2024-04-19 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_register_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=2),
        ),
    ]
