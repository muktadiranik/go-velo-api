# Generated by Django 4.0.8 on 2023-01-23 09:06

from django.db import migrations
import django_quill.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_aboutus_content_aboutus_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='short_description',
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='description',
            field=django_quill.fields.QuillField(),
        ),
    ]
