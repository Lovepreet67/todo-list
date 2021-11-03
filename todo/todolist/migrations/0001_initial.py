# Generated by Django 3.2.6 on 2021-11-02 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('task_disc', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='relation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('task_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todolist.task', verbose_name='task_id')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todolist.user', verbose_name='user_id')),
            ],
        ),
    ]
