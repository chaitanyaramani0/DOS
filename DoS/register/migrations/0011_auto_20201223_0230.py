# Generated by Django 3.1.4 on 2020-12-23 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0010_auto_20201223_0227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='customer_id',
            field=models.CharField(default='OJYPST6W2U', editable=False, max_length=10),
        ),
    ]
