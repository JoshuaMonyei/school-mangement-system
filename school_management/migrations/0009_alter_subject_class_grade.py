# Generated by Django 4.1.4 on 2023-01-30 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0008_subject_credit_unit_alter_subject_class_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='class_grade',
            field=models.CharField(choices=[('freshman', 'freshman'), ('sophomore', 'sophomore'), ('junior', 'junior'), ('senior', 'senior')], default='freshman', max_length=255),
        ),
    ]
