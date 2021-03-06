# Generated by Django 3.2.6 on 2021-11-02 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.RemoveField(
            model_name='relation',
            name='task_id',
        ),
        migrations.RemoveField(
            model_name='relation',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='task',
            name='task_id',
        ),
        migrations.AddField(
            model_name='relation',
            name='task_r',
            field=models.ForeignKey(default='0000000', on_delete=django.db.models.deletion.CASCADE, to='todolist.task', verbose_name='task_id'),
        ),
        migrations.AddField(
            model_name='task',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='user',
        ),
        migrations.AddField(
            model_name='relation',
            name='user_r',
            field=models.ForeignKey(default='0000000', on_delete=django.db.models.deletion.CASCADE, to='todolist.user_field', verbose_name='user_id'),
        ),
    ]
