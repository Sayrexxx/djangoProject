# Generated by Django 4.2.4 on 2024-05-23 00:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toyFactory', '0006_alter_order_delivery_date_alter_purchase_purchase_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='delivery_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 26, 0, 47, 29, 518686, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='purchase_id',
            field=models.IntegerField(default=41936),
        ),
    ]