# Generated by Django 4.2 on 2024-04-22 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_alter_grade_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registers', to='app.course'),
        ),
        migrations.AlterField(
            model_name='register',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='registers', to='app.student'),
        ),
    ]
