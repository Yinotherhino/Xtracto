# Generated by Django 4.0.1 on 2022-07-26 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registered',
            fields=[
                ('userName', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('passWord', models.CharField(max_length=50)),
            ],
        ),
    ]
