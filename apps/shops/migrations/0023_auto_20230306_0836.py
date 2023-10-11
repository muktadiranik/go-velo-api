# Generated by Django 3.2.15 on 2023-03-06 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0022_auto_20230306_0714'),
    ]

    operations = [
        migrations.AddField(
            model_name='pickuplocation',
            name='latitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='pickuplocation',
            name='longitude',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]