# Generated by Django 4.2.4 on 2023-08-17 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_blog_view_counts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='view_counts',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
