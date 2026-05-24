from django.contrib import admin
from .models import Appointment

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'get_doctor_display', 'date', 'time', 'created_at')
    list_filter = ('doctor', 'date')
    search_fields = ('name', 'phone')
    ordering = ('date', 'time')
