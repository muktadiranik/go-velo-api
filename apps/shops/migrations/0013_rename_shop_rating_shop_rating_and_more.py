# Generated by Django 4.0.8 on 2023-02-02 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0012_shop_shop_rating_shop_shop_reviews'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='shop_rating',
            new_name='rating',
        ),
        migrations.RenameField(
            model_name='shop',
            old_name='shop_reviews',
            new_name='total_reviews',
        ),
    ]
