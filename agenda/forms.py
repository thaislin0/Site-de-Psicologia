from django import forms
from tempus_dominus.widgets import DatePicker, TimePicker
from datetime import datetime


class AgendaForms(forms.Form):
    Nome = forms.CharField(label='Nome')
    Sobrenome = forms.CharField(label='Sobrenome')
    Email = forms.EmailField(label='Email')
    Data = forms.DateField(label='Data', widget=DatePicker())
    Hora = forms.TimeField(label='Hora', widget=TimePicker(options={
                'enabledHours': [19, 20, 21, 22]}))
