# Generated by Django 5.0.9 on 2024-10-18 23:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_student_teacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('attendance_count', models.BigIntegerField(default=0)),
                ('completion_count', models.BigIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=50)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student')),
            ],
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('attendance_count', models.IntegerField(default=0)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='LessonCompletion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completion_date', models.DateTimeField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.lesson')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.student')),
            ],
        ),
    ]
