# Generated by Django 4.2 on 2024-04-19 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_grade_grade'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='register',
        ),
        migrations.AddField(
            model_name='register',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.subject'),
            preserve_default=False,
        ),
    ]
