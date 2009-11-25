from django import forms
from events.models import Event, City

class EventForm(forms.ModelForm):
   city = forms.ModelChoiceField(City.objects.all(), empty_label=None, label="Ville")

   class Meta:
        model = Event
        exclude = ('submission_time', 'updated_time', 'decision_time',
                   'moderator', 'moderated', 'latitude', 'longitude')

