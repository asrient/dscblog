# Generated by Django 3.1.1 on 2020-10-04 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dscblog', '0008_follower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=models.CharField(default='', max_length=3500, verbose_name='Content'),
        ),
    ]
