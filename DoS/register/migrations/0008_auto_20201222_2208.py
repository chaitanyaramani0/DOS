# Generated by Django 3.1.4 on 2020-12-22 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_auto_20201222_2048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pickup',
            old_name='pickup_date',
            new_name='schedule_date',
        ),
        migrations.AlterField(
            model_name='bulk',
            name='customer_id',
            field=models.CharField(default='B0KUWFT8LY', editable=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='commercial',
            name='customer_id',
            field=models.CharField(default='E5P6AXNHBQ', editable=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='individual',
            name='customer_id',
            field=models.CharField(default='VU1AJDTKKL', editable=False, max_length=10),
        ),
        migrations.AlterField(
            model_name='industrial',
            name='customer_id',
            field=models.CharField(default='AHZBVPPNEG', editable=False, max_length=10),
        ),
    ]