# Generated by Django 3.1.1 on 2020-11-04 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dscblog', '0015_view'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('name', models.CharField(max_length=30, primary_key=True, serialize=False, verbose_name='Name')),
                ('created_on', models.DateTimeField()),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='topics',
            field=models.ManyToManyField(related_name='blogs', to='dscblog.Topic'),
        ),
    ]
