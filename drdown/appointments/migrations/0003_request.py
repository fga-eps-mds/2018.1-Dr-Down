# Generated by Django 2.0.3 on 2018-05-06 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0002_auto_20180506_1956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift', models.CharField(choices=[('M', 'Morning'), ('A', 'Afternoon')], help_text='Shift of appointment', max_length=10, verbose_name='Shift')),
                ('motive', models.TextField(blank=True, help_text='Why are you requesting an appointment?', max_length=500, verbose_name='Motive')),
                ('observation', models.TextField(blank=True, help_text='Why was it scheduled/declined?', max_length=500, verbose_name='Observation')),
                ('speciality', models.CharField(choices=[('Speech Therapy', 'Speech Therapy'), ('Psychology', 'Psychology'), ('Physiotherapy', 'Physiotherapy'), ('Occupational Therapy', 'Occupational Therapy'), ('Cardiology', 'Cardiology'), ('Neurology', 'Neurology'), ('Pediatrics', 'Pediatrics')], help_text='Speciality of appointment', max_length=30, verbose_name='Speciality')),
                ('status', models.CharField(default='Pending', editable=False, help_text='Was the request accepted?', max_length=20, verbose_name='Status')),
                ('doctor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='users.HealthTeam', verbose_name='Doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='users.Patient', verbose_name='Patient')),
            ],
            options={
                'verbose_name': 'Request',
                'verbose_name_plural': 'Requests',
            },
        ),
    ]