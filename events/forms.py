# -*- encoding:utf-8 -*-
from django import forms
from events.models import Event, City, Region
from django.forms.util import ErrorList
from datetime import datetime

class EventForm(forms.ModelForm):
    city = forms.ModelChoiceField(City.objects.all(), empty_label=None, label="Ville")

    class Meta:
      model = Event
      exclude = ('submission_time', 'updated_time', 'decision_time',
                 'moderator', 'moderated', 'latitude', 'longitude')

    def clean(self):
      cleaned_data = self.cleaned_data
      start_time = cleaned_data.get("start_time")
      end_time = cleaned_data.get("end_time")

      if start_time >= end_time:
        msg = u"L'évènement ne peut se terminer avant son début"
        self._errors["start_time"] = ErrorList([msg])
        self._errors["end_time"] = ErrorList([msg])

        del cleaned_data["start_time"]
        del cleaned_data["end_time"]

      elif start_time < datetime.today():
        msg = u"Seul les évènements à venir sont acceptés"
        self._errors["start_time"] = ErrorList([msg])

        del cleaned_data["start_time"]

      return cleaned_data

class RegionFilterForm (forms.Form):
    region = forms.ModelChoiceField(Region.objects.all(), empty_label="Toutes les régions", required=False, label="Région",
        widget=forms.Select(attrs={'onchange':'document.getElementById("filter").submit();'}))

