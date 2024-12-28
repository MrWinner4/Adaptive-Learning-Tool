# Generated by Django 4.2.17 on 2024-12-28 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_alter_lesson_lecture'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(default='example question')),
                ('option_a', models.CharField(max_length=250)),
                ('option_b', models.CharField(max_length=250)),
                ('option_c', models.CharField(max_length=250)),
                ('option_d', models.CharField(max_length=250)),
                ('correct_answer', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], max_length=1)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='lessons.quiz')),
            ],
        ),
    ]