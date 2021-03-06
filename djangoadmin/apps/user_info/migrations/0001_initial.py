# Generated by Django 2.2 on 2021-04-06 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'MALE'), ('F', 'FEMALE')], max_length=255)),
            ],
        ),
    ]
