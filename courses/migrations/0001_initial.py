# Generated by Django 4.1.7 on 2023-02-21 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('preview', models.ImageField(null=True, upload_to='courses/previews')),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]
