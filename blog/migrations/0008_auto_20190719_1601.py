# Generated by Django 2.2.3 on 2019-07-19 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20190719_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag_set',
            field=models.ManyToManyField(blank=True, to='blog.Tag'),
        ),
    ]
