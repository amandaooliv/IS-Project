# Generated by Django 4.2 on 2024-04-20 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_grade_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='grade',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='grade',
            name='status',
            field=models.CharField(blank=True, choices=[('Aprovado', 'Aprovado'), ('Reprovado', 'Reprovado'), ('Sem nota', 'Sem nota')], max_length=10, null=True),
        ),
    ]
