from django import forms

from .models import Journal


class JournalForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ("name", "date", 'wens', 'thurs', 'fri', 'satur', 'sun', 'mon', 'tues', 'journal')
