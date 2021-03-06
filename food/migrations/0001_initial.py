# Generated by Django 3.0 on 2022-06-21 12:20

from django.db import migrations, models
import food.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('en_name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to=food.models.upload_food_img)),
            ],
        ),
    ]
