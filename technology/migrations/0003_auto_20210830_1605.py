# Generated by Django 3.0.3 on 2021-08-30 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0002_resumetech'),
    ]

    operations = [
        migrations.AlterField(
            model_name='technology',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]