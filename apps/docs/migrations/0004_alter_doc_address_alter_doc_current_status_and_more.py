# Generated by Django 4.1.5 on 2023-10-05 22:50

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('corecode', '0009_delete_document'),
        ('employees', '0010_alter_employee_date_of_dismissal'),
        ('docs', '0003_remove_doc_citizenship_doc_date_of_preparing_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doc',
            name='address',
            field=models.TextField(blank=True, verbose_name='Address in the Russian Federation'),
        ),
        migrations.AlterField(
            model_name='doc',
            name='current_status',
            field=models.CharField(choices=[('active', 'active'), ('inactive', 'inactive')], default='active', max_length=10, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='doc',
            name='date_of_expiry',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Valid until'),
        ),
        migrations.AlterField(
            model_name='doc',
            name='date_of_issue',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='date of issue'),
        ),
        migrations.AlterField(
            model_name='doc',
            name='date_of_preparing',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Start ordering before'),
        ),
        migrations.AlterField(
            model_name='doc',
            name='doc_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='corecode.documenttype', verbose_name='Document type'),
        ),
        migrations.AlterField(
            model_name='doc',
            name='employee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='employees.employee', verbose_name='Employee'),
        ),
        migrations.AlterField(
            model_name='doc',
            name='issued_authority',
            field=models.CharField(max_length=200, verbose_name='Issued by'),
        ),
        migrations.AlterField(
            model_name='doc',
            name='number',
            field=models.CharField(max_length=200, verbose_name='Number No.'),
        ),
        migrations.AlterField(
            model_name='doc',
            name='others',
            field=models.TextField(blank=True, verbose_name='Other'),
        ),
        migrations.AlterField(
            model_name='doc',
            name='scanned_doc',
            field=models.FileField(blank=True, upload_to='docs/uploads/', verbose_name='Upload file'),
        ),
        migrations.AlterField(
            model_name='doc',
            name='serial',
            field=models.CharField(max_length=200, verbose_name='Series'),
        ),
    ]
