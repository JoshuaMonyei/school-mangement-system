# Generated by Django 4.1.4 on 2023-01-29 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0007_subject_class_grade_alter_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='credit_unit',
            field=models.IntegerField(default=2),
        ),
        migrations.AlterField(
            model_name='subject',
            name='class_grade',
            field=models.CharField(choices=[('freshman', 'freshman'), ('sophomore', 'sophomore'), ('junior', 'junior'), ('senior', 'senior')], default='junior', max_length=255),
        ),
    ]
