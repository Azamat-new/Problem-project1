from django.db import models

DOCTOR_CHOICES = [
    ('therapist', 'Терапевт'),
    ('cardiologist', 'Кардиолог'),
    ('neurologist', 'Невролог'),
    ('surgeon', 'Хирург'),
    ('dentist', 'Стоматолог'),
    ('pediatrician', 'Педиатр'),
    ('allergist', 'Аллерголог'),
]

class Appointment(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя пациента')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    doctor = models.CharField(max_length=50, choices=DOCTOR_CHOICES, verbose_name='Специалист')
    date = models.DateField(verbose_name='Дата приёма')
    time = models.TimeField(verbose_name='Время приёма')
    note = models.TextField(blank=True, verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
        ordering = ['date', 'time']

    def __str__(self):
        return f"{self.name} — {self.get_doctor_display()} — {self.date} {self.time}"
