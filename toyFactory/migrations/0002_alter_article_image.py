# Generated by Django 4.2.4 on 2024-05-17 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toyFactory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
