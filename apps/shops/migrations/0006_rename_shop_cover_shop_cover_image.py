# Generated by Django 4.0.8 on 2023-01-30 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0005_shop_shop_cover'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='shop_cover',
            new_name='cover_image',
        ),
    ]
