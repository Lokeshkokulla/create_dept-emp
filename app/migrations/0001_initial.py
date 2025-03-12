# Generated by Django 5.1.5 on 2025-03-06 06:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DEPT',
            fields=[
                ('dept_no', models.IntegerField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=100)),
                ('dloc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SALGRADE',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('high_sal', models.DecimalField(decimal_places=3, max_digits=10)),
                ('low_sal', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='EMP',
            fields=[
                ('empno', models.IntegerField(primary_key=True, serialize=False)),
                ('ename', models.CharField(max_length=100)),
                ('job', models.CharField(max_length=100)),
                ('sal', models.DecimalField(decimal_places=3, max_digits=10)),
                ('comm', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('hiredate', models.DateField(auto_now=True)),
                ('MGR', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.emp')),
                ('dept_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.dept')),
            ],
        ),
    ]
