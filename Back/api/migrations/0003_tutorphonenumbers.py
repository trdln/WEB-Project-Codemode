# Generated by Django 4.0.3 on 2022-04-17 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_tutor_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='TutorPhoneNumbers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='api.tutor')),
            ],
        ),
    ]