# Generated by Django 4.2.4 on 2023-08-22 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_blog_view_counts'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-view_counts', '-updated_on'], 'verbose_name': 'Content', 'verbose_name_plural': 'My Contents'},
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, max_length=300),
        ),
    ]
