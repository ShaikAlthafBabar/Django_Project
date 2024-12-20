# Generated by Django 5.0.6 on 2024-12-13 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('watchlistApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='streamingPlatform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(max_length=100)),
                ('about', models.CharField(max_length=150)),
                ('website', models.URLField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='watchList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
    ]