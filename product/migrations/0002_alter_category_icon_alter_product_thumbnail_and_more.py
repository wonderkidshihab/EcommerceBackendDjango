# Generated by Django 4.1.3 on 2022-11-28 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='./static/icons'),
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='./static/product/thumbnail'),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.ImageField(upload_to='./static/product/images'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='./static/icons'),
        ),
    ]
