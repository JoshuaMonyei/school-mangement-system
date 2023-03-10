# Generated by Django 4.1.4 on 2023-01-17 08:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminHOD',
            fields=[
                ('id', models.UUIDField(default='5012e2cb0c024aa4b8d780d61d802f58', editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.UUIDField(default='5012e2cb0c024aa4b8d780d61d802f58', editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('attendance_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AttendanceReport',
            fields=[
                ('id', models.UUIDField(default='5012e2cb0c024aa4b8d780d61d802f58', editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.UUIDField(default='5012e2cb0c024aa4b8d780d61d802f58', editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('department_name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FeedBackStaff',
            fields=[
                ('id', models.UUIDField(default='5012e2cb0c024aa4b8d780d61d802f58', editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('feedback', models.TextField()),
                ('feedback_reply', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FeedBackStudent',
            fields=[
                ('id', models.UUIDField(default='5012e2cb0c024aa4b8d780d61d802f58', editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('feedback', models.TextField()),
                ('feedback_reply', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LeaveReportStaff',
            fields=[
                ('id', models.UUIDField(default='5012e2cb0c024aa4b8d780d61d802f58', editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('leave_date', models.CharField(max_length=255)),
                ('leave_message', models.TextField()),
                ('leave_status', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LeaveReportStudent',
            fields=[
                ('id', models.UUIDField(default='5012e2cb0c024aa4b8d780d61d802f58', editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('leave_date', models.CharField(max_length=255)),
                ('leave_message', models.TextField()),
                ('leave_status', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NotificationStaff',
            fields=[
                ('id', models.UUIDField(default='5012e2cb0c024aa4b8d780d61d802f58', editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('message', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NotificationStudent',
            fields=[
                ('id', models.UUIDField(default='5012e2cb0c024aa4b8d780d61d802f58', editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('message', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.UUIDField(default='5012e2cb0c024aa4b8d780d61d802f58', editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('address', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default='5012e2cb0c024aa4b8d780d61d802f58', editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('gender', models.CharField(max_length=255)),
                ('profile_pic', models.FileField(upload_to='')),
                ('address', models.TextField()),
                ('session_start_year', models.DateField()),
                ('session_end_year', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.UUIDField(default='5012e2cb0c024aa4b8d780d61d802f58', editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('subject_name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default='5012e2cb0c024aa4b8d780d61d802f58', editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('auth0_user_id', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=255)),
                ('profile_pic', models.FileField(upload_to='')),
                ('address', models.TextField()),
                ('session_start_year', models.DateField(auto_now=True)),
                ('session_end_year', models.DateField(blank=True)),
                ('role', models.IntegerField(choices=[(1, 'HOD'), (2, 'staff'), (3, 'student')], default=3)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
