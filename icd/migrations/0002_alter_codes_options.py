# Generated by Django 4.0.4 on 2022-05-02 17:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('icd', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='codes',
            options={'ordering': ['-updated', '-created']},
        ),
    ]
