# Generated by Django 2.1.3 on 2018-11-05 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('circuits', '0013_cables'),
    ]

    operations = [
        migrations.AddField(
            model_name='circuittermination',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
