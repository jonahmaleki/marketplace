# Generated by Django 4.2 on 2023-04-18 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_comment_author_alter_comment_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(verbose_name='write your comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='recommend',
            field=models.BooleanField(default=True, verbose_name='i recommend this product'),
        ),
    ]