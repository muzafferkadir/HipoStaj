# Generated by Django 2.2.1 on 2019-05-11 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_auto_20190510_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='recipe/'),
        ),
    ]
