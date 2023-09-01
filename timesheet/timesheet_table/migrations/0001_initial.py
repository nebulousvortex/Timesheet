# Generated by Django 4.2.4 on 2023-08-22 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Тип пары')),
            ],
        ),
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='День недели')),
            ],
        ),
        migrations.CreateModel(
            name='WeekType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Тип недели')),
            ],
        ),
        migrations.CreateModel(
            name='Timesheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(verbose_name='Время')),
                ('name', models.TextField(verbose_name='Название')),
                ('room', models.TextField(verbose_name='Аудитория')),
                ('teacher', models.TextField(verbose_name='Преподаватель')),
                ('day', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='timesheet_table.days')),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='timesheet_table.classtype')),
                ('week', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='timesheet_table.weektype')),
            ],
        ),
    ]