# Generated by Django 4.1.7 on 2023-03-29 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rhyme', '0004_alter_rhymes_rhyme_alter_word_stressed_word_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='all_stresses',
            field=models.JSONField(default=''),
        ),
        migrations.AlterField(
            model_name='word',
            name='stressed_word',
            field=models.CharField(default='', max_length=100),
        ),
    ]
