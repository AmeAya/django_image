# Generated by Django 5.1.3 on 2024-11-27 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paintings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='paintings')),
            ],
        ),
    ]
