# Generated by Django 3.2 on 2022-04-12 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20220412_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='time_post',
            field=models.DateTimeField(),
        ),
    ]