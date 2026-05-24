from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя пациента')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('doctor', models.CharField(choices=[('therapist', 'Терапевт'), ('cardiologist', 'Кардиолог'), ('neurologist', 'Невролог'), ('surgeon', 'Хирург'), ('dentist', 'Стоматолог'), ('pediatrician', 'Педиатр'), ('allergist', 'Аллерголог')], max_length=50, verbose_name='Специалист')),
                ('date', models.DateField(verbose_name='Дата приёма')),
                ('time', models.TimeField(verbose_name='Время приёма')),
                ('note', models.TextField(blank=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Записи',
                'ordering': ['date', 'time'],
            },
        ),
    ]
