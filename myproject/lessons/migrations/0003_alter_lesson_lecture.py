# Generated by Django 4.2.17 on 2024-12-26 18:20

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0002_lesson_description_lesson_lecture_lesson_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='lecture',
            field=ckeditor.fields.RichTextField(default='example lecture'),
        ),
    ]
