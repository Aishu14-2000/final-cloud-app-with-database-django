# Generated by Django 3.1.3 on 2022-08-04 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='choice_correct',
            new_name='is_correct',
        ),
        migrations.RemoveField(
            model_name='choice',
            name='Choice_content',
        ),
        migrations.RemoveField(
            model_name='question',
            name='mark',
        ),
        migrations.RemoveField(
            model_name='question',
            name='question_text',
        ),
        migrations.AddField(
            model_name='choice',
            name='text',
            field=models.CharField(default='question text', max_length=550),
        ),
        migrations.AddField(
            model_name='question',
            name='grade',
            field=models.FloatField(default=5.0),
        ),
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.CharField(default='question text', max_length=550),
        ),
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.CharField(default='question title', max_length=550),
        ),
    ]
