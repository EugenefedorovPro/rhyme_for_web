# Generated by Django 4.1.7 on 2023-03-28 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rhyme', '0003_alter_word_stressed_word'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rhymes',
            name='rhyme',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='word',
            name='stressed_word',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='word',
            name='unstressed_word',
            field=models.CharField(max_length=100),
        ),
    ]
