# Generated by Django 5.0.4 on 2024-05-03 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TopsisResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rank', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('score', models.FloatField()),
            ],
        ),
    ]
