# Generated by Django 4.2.4 on 2023-08-21 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
