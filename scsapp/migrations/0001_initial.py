# Generated by Django 4.2.7 on 2024-09-17 05:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=50)),
                ('job', models.CharField(max_length=50)),
                ('salary', models.IntegerField(default=0)),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scsapp.dept')),
            ],
        ),
    ]
