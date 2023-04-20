# Generated by Django 4.2 on 2023-04-19 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_comment_body_alter_comment_recommend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='stars',
            field=models.CharField(choices=[('1', 'Very bad'), ('2', 'Bad'), ('3', 'Normal'), ('4', 'Good'), ('5', 'Perfect')], max_length=10, verbose_name='your score to this product'),
        ),
    ]
