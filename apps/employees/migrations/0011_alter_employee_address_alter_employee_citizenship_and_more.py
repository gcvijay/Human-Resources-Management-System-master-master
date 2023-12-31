# Generated by Django 4.1.5 on 2023-10-05 22:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0009_delete_document'),
        ('employees', '0010_alter_employee_date_of_dismissal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='address',
            field=models.TextField(blank=True, verbose_name='Address in the Russian Federation'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='citizenship',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='corecode.citizenship', verbose_name='Citizenship'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='current_doc_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='corecode.permitdoccategory', verbose_name='Document category'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='current_status',
            field=models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=10, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_of_dismissal',
            field=models.DateField(verbose_name='Date of dismissal'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_of_employment',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='date of receipt'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='firstname',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=10, verbose_name='Floor'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=13, validators=[django.core.validators.RegexValidator(message="Entered mobile number isn't in a right format!", regex='^[0-9]{10,15}$')], verbose_name='Tel number'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='other_name',
            field=models.CharField(blank=True, max_length=200, verbose_name='Surname'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='others',
            field=models.TextField(blank=True, verbose_name='Other'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='personnel_number',
            field=models.CharField(max_length=200, unique=True, verbose_name='Personnel Number'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='photo',
            field=models.ImageField(blank=True, upload_to='employees/photos/', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(max_length=200, verbose_name='Job title'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='snils_number',
            field=models.CharField(blank=True, max_length=200, verbose_name='SNILS'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='surname',
            field=models.CharField(max_length=200, verbose_name='Surname'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='tin_number',
            field=models.CharField(blank=True, max_length=200, verbose_name='TIN'),
        ),
    ]
