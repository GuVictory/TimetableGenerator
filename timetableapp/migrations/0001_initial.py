# Generated by Django 3.2 on 2021-04-26 08:02

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('activity_id', models.CharField(max_length=2000, primary_key=True, serialize=False)),
                ('activity_type', models.CharField(choices=[('Fixed', 'Fixed'), ('Replaceable', 'Replaceable')], max_length=2000, null=True)),
                ('class_id', models.CharField(max_length=2000, null=True)),
                ('classroom_id', models.CharField(max_length=2000, null=True)),
                ('course_id', models.CharField(max_length=2000, null=True)),
                ('professor_id', models.CharField(max_length=2000, null=True)),
                ('day', models.CharField(max_length=2000, null=True)),
                ('start_time', models.PositiveIntegerField(null=True)),
                ('end_time', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('class_id', models.CharField(max_length=2000, primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=2000, null=True)),
                ('week_day', multiselectfield.db.fields.MultiSelectField(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=2000)),
                ('start_time', models.PositiveIntegerField(null=True)),
                ('end_time', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('classroom_id', models.CharField(max_length=2000, primary_key=True, serialize=False)),
                ('classroom_name', models.CharField(max_length=2000, null=True)),
                ('classroom_type', models.CharField(choices=[('Theory', 'Theory'), ('Lab', 'Lab')], max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(max_length=1000, primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=1000, null=True)),
                ('course_type', models.CharField(choices=[('Theory', 'Theory'), ('Lab', 'Lab')], max_length=200, null=True)),
                ('credit_hours', models.IntegerField(null=True)),
                ('contact_hours', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('professor_id', models.CharField(max_length=2000, primary_key=True, serialize=False)),
                ('professor_name', models.CharField(max_length=2000, null=True)),
                ('working_hours', models.IntegerField(null=True)),
                ('available_hours', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SectionClassroom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='timetableapp.class')),
                ('classroom_id', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='timetableapp.classroom')),
            ],
            options={
                'unique_together': {('class_id', 'classroom_id')},
            },
        ),
        migrations.CreateModel(
            name='ClassCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetableapp.class')),
                ('course_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetableapp.course')),
                ('professor_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='timetableapp.professor')),
            ],
            options={
                'unique_together': {('class_id', 'course_id')},
            },
        ),
    ]
