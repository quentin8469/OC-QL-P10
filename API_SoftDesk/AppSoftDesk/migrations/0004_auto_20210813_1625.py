# Generated by Django 3.2.6 on 2021-08-13 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppSoftDesk', '0003_rename_tile_issues_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comments',
            options={'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='contributors',
            options={'verbose_name': 'Contributor', 'verbose_name_plural': 'Contributors'},
        ),
        migrations.AlterModelOptions(
            name='issues',
            options={'verbose_name': 'Issue', 'verbose_name_plural': 'Issues'},
        ),
        migrations.AlterModelOptions(
            name='projects',
            options={'verbose_name': 'Project', 'verbose_name_plural': 'Projects'},
        ),
    ]
