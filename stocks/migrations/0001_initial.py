# Generated by Django 5.1.5 on 2025-01-22 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('price', models.FloatField(null=True)),
                ('moment', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
