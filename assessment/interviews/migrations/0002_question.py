# Generated by Django 5.1.6 on 2025-02-21 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interviews', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField()),
                ('category', models.CharField(choices=[('HR', 'HR Interview'), ('TECHNICAL', 'Technical Interview'), ('GENERAL', 'General Communication')], max_length=20)),
                ('difficulty', models.IntegerField(default=1)),
            ],
        ),
    ]
