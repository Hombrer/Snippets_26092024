# Generated by Django 5.1.1 on 2024-09-27 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_snippet_public'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='snippet',
            options={'ordering': ['name', 'lang']},
        ),
    ]
