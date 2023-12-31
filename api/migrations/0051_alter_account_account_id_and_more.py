# Generated by Django 4.1.2 on 2023-12-31 07:30

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0050_alter_account_account_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='account_id',
            field=models.CharField(blank=True, default=api.models.generate_uuid4_hex, max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bestsubmission',
            name='best_submission_id',
            field=models.CharField(blank=True, default=api.models.generate_uuid4_hex, max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='collection',
            name='collection_id',
            field=models.CharField(blank=True, default=api.models.generate_uuid4_hex, max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='collectiongrouppermission',
            name='collection_group_permission_id',
            field=models.CharField(blank=True, default=api.models.generate_uuid4_hex, max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='collectionproblem',
            name='id',
            field=models.CharField(blank=True, default=api.models.generate_uuid4_hex, max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_id',
            field=models.CharField(blank=True, default=api.models.generate_uuid4_hex, max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='groupmember',
            name='group_member_id',
            field=models.CharField(blank=True, default=api.models.generate_uuid4_hex, max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='problem',
            name='problem_id',
            field=models.CharField(blank=True, default=api.models.generate_uuid4_hex, max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='problemgrouppermission',
            name='problem_group_permission_id',
            field=models.CharField(blank=True, default=api.models.generate_uuid4_hex, max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='submission',
            name='submission_id',
            field=models.CharField(blank=True, default=api.models.generate_uuid4_hex, max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='submissiontestcase',
            name='submission_testcase_id',
            field=models.CharField(blank=True, default=api.models.generate_uuid4_hex, max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='testcase_id',
            field=models.CharField(blank=True, default=api.models.generate_uuid4_hex, max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='topic',
            name='topic_id',
            field=models.CharField(blank=True, default=api.models.generate_uuid4_hex, max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='topiccollection',
            name='id',
            field=models.CharField(blank=True, default=api.models.generate_uuid4_hex, max_length=32, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='topicgrouppermission',
            name='topic_group_permission_id',
            field=models.CharField(blank=True, default=api.models.generate_uuid4_hex, max_length=32, primary_key=True, serialize=False),
        ),
    ]
