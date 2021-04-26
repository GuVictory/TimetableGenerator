# Generated by Django 3.2 on 2021-04-26 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetableapp', '0003_alter_course_course_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='classroom_type',
            field=models.CharField(choices=[('Theory', 'Лекционная'), ('Lab', 'Семинарская')], max_length=2000, null=True),
        ),
    ]