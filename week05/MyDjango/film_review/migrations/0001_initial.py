# Generated by Django 2.2.13 on 2020-09-24 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='T1',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('stars', models.IntegerField()),
                ('comment', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 't1',
                'managed': False,
            },
        ),
    ]