# Generated by Django 4.2 on 2024-04-16 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_register_subject_remove_subject_student_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='app.course'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='register',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.register'),
        ),
    ]