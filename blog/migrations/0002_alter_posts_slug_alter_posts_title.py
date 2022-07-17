# Generated by Django 4.0.6 on 2022-07-05 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='slug',
            field=models.SlugField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='posts',
            name='title',
            field=models.CharField(max_length=500, verbose_name='Title'),
        ),
    ]
