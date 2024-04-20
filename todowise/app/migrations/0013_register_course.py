# Generated by Django 4.2 on 2024-04-16 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_remove_register_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='course',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='registers', to='app.course'),
        ),
    ]
