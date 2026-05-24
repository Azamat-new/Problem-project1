from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Appointment

def home(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save()
            return redirect('success', pk=appointment.pk)
    else:
        form = AppointmentForm()
    return render(request, 'register.html', {'form': form})

def success(request, pk):
    appointment = Appointment.objects.get(pk=pk)
    return render(request, 'success.html', {'appointment': appointment})
