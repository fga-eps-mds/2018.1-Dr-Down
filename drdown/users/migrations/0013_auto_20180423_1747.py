# Generated by Django 2.0.3 on 2018-04-23 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20180423_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthteam',
            name='council_acronym',
            field=models.CharField(choices=[('CRM', 'CRM'), ('CRP', 'CRP'), ('COFFITO', 'COFFITO'), ('COREN', 'COREN'), ('CREFONO', 'CREFONO')], help_text='The Regional Council.', max_length=30, verbose_name='Council Acronym'),
        ),
        migrations.AlterField(
            model_name='healthteam',
            name='speciality',
            field=models.CharField(choices=[('Speech Therapy', 'Speech Therapy'), ('Psychology', 'Psychology'), ('Physiotherapy', 'Physiotherapy'), ('Occupational Therapy', 'Occupational Therapy'), ('Doctor', 'Doctor'), ('Cardiology', 'Cardiology'), ('Neurology', 'Neurology'), ('Pediatrics', 'Pediatrics'), ('Nurse', 'Nurse')], help_text='The speciality that this member of health team works.', max_length=30, verbose_name='Speciality'),
        ),
    ]
