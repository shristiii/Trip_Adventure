# Generated by Django 4.0.2 on 2022-03-18 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_userblog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userblog',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
