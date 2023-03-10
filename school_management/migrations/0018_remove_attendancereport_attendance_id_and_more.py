# Generated by Django 4.1.4 on 2023-02-08 04:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school_management', '0017_user_istuitionpaid_alter_user_campus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendancereport',
            name='attendance_id',
        ),
        migrations.RemoveField(
            model_name='attendancereport',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='feedbackstaff',
            name='staff_id',
        ),
        migrations.RemoveField(
            model_name='feedbackstudent',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='leavereportstaff',
            name='staff_id',
        ),
        migrations.RemoveField(
            model_name='leavereportstudent',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='notificationstaff',
            name='staff_id',
        ),
        migrations.RemoveField(
            model_name='notificationstudent',
            name='student_id',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='isTuitionPaid',
            new_name='tuitionPaid',
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='AttendanceReport',
        ),
        migrations.DeleteModel(
            name='FeedBackStaff',
        ),
        migrations.DeleteModel(
            name='FeedBackStudent',
        ),
        migrations.DeleteModel(
            name='LeaveReportStaff',
        ),
        migrations.DeleteModel(
            name='LeaveReportStudent',
        ),
        migrations.DeleteModel(
            name='NotificationStaff',
        ),
        migrations.DeleteModel(
            name='NotificationStudent',
        ),
    ]
