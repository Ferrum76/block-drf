# Generated by Django 5.1 on 2024-10-08 11:40

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0002_course_student_lesson_student"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="course",
            name="student",
        ),
        migrations.RemoveField(
            model_name="lesson",
            name="student",
        ),
        migrations.AddField(
            model_name="course",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец курса",
            ),
        ),
        migrations.AddField(
            model_name="lesson",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Владелец урока",
            ),
        ),
    ]
