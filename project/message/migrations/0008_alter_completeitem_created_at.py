# Generated by Django 4.2.7 on 2023-11-22 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0007_category_head_image_alter_askitem_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completeitem',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
