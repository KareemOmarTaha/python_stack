# Generated by Django 4.2.1 on 2023-06-03 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0002_author_notes'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='desc',
            field=models.TextField(default='No Comment'),
        ),
    ]
