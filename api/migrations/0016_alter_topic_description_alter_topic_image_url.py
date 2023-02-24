# Generated by Django 4.1.2 on 2023-02-23 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_remove_topic_image_topic_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to='topic/'),
        ),
    ]
