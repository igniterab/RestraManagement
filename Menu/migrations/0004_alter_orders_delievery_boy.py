# Generated by Django 4.0.6 on 2022-07-13 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
        ('Menu', '0003_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='delievery_boy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.staffuser'),
        ),
    ]
