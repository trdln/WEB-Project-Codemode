# Generated by Django 4.0.4 on 2022-04-25 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_coursetutor_options_alter_money_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentCourseComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=512)),
            ],
            options={
                'verbose_name': "Student's course comment",
                'verbose_name_plural': "Students' course comments",
            },
        ),
        migrations.RemoveField(
            model_name='student',
            name='courses',
        ),
        migrations.AddField(
            model_name='course',
            name='commented_by',
            field=models.ManyToManyField(through='api.StudentCourseComment', to='api.student'),
        ),
        migrations.AddField(
            model_name='coursetutor',
            name='students',
            field=models.ManyToManyField(related_name='courses', through='api.StudentCourseTutor', to='api.student'),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='image_url',
            field=models.URLField(blank=True, default='', max_length=300),
        ),
        migrations.AddField(
            model_name='studentcoursecomment',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.course'),
        ),
        migrations.AddField(
            model_name='studentcoursecomment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.student'),
        ),
    ]
