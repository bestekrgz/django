# Generated by Django 4.0.1 on 2022-04-26 22:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yourturnapp', '0005_alter_project_options_review_owner_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='body',
            new_name='comment',
        ),
    ]