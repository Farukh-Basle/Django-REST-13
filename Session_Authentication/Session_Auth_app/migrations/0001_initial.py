# Generated by Django 3.1 on 2021-05-14 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('eno', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=40)),
                ('esal', models.IntegerField()),
                ('email', models.EmailField(blank=True, max_length=255, null=True, unique=True)),
            ],
        ),
    ]
