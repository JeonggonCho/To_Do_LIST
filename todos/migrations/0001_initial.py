# Generated by Django 3.2.18 on 2023-03-30 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('content', models.TextField()),
                ('completed', models.BooleanField(default=False)),
                ('priority', models.IntegerField(default=3)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('deadline', models.DateField(null=True)),
            ],
        ),
    ]
