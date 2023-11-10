# Generated by Django 3.2.23 on 2023-11-10 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('size', models.IntegerField()),
                ('image', models.ImageField(default='type', upload_to='type')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField(default='orderItems')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(max_length=5)),
                ('location', models.TextField(default='my location')),
                ('image', models.ImageField(default='my profile', upload_to='my profile')),
            ],
        ),
    ]
