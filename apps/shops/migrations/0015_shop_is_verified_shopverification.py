# Generated by Django 4.0.8 on 2023-02-06 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0014_alter_shop_shop_cover_alter_shop_shop_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='ShopVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=50)),
                ('owner_image', models.ImageField(blank=True, null=True, upload_to='shops/verification/owner')),
                ('id_front_image', models.ImageField(blank=True, null=True, upload_to='shops/verification/id_front')),
                ('id_back_image', models.ImageField(blank=True, null=True, upload_to='shops/verification/id_back')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('shop', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shops.shop')),
            ],
        ),
    ]