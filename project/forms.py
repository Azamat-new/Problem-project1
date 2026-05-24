from django import forms
from .models import Appointment
import datetime

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['name', 'phone', 'doctor', 'date', 'time', 'note']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Ваше имя',
                'class': 'form-input',
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': '+996 700 000 000',
                'class': 'form-input',
            }),
            'doctor': forms.Select(attrs={
                'class': 'form-input',
            }),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-input',
                'min': datetime.date.today().isoformat(),
            }),
            'time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'form-input',
            }),
            'note': forms.Textarea(attrs={
                'placeholder': 'Опишите причину обращения (необязательно)',
                'class': 'form-input',
                'rows': 3,
            }),
        }

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date and date < datetime.date.today():
            raise forms.ValidationError('Нельзя записаться на прошедшую дату.')
        if date and date.weekday() in (5, 6):
            raise forms.ValidationError('Запись доступна только в рабочие дни (Пн–Пт).')
        return date
