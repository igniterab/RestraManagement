# Generated by Django 4.0.6 on 2022-07-13 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='reciepe',
            field=models.JSONField(default={}),
            preserve_default=False,
        ),
    ]