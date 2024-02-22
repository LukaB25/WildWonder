# Generated by Django 4.2.10 on 2024-02-21 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_comment_updated_on_alter_comment_author_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='rating',
            new_name='user_vote',
        ),
        migrations.RemoveField(
            model_name='post',
            name='rating',
        ),
        migrations.AddField(
            model_name='vote',
            name='vote_total',
            field=models.FloatField(default=0),
        ),
    ]