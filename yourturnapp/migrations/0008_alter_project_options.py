# Generated by Django 4.0.1 on 2022-04-28 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yourturnapp', '0007_alter_review_owner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['-vote_ratio', '-vote_total']},
        ),
    ]
