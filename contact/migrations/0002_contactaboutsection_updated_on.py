# Generated by Django 4.2.10 on 2024-02-13 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactaboutsection',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]