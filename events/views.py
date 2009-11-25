from datetime import date, timedelta
from django.shortcuts import render_to_response, HttpResponseRedirect
from events.forms import EventForm

def propose (request):
  form = EventForm (request)

  if request.method == 'POST':
    form = EventForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/event/new/thanks/')
  else:
    form = EventForm()

  return render_to_response('events/event_new.html', {
    'form': form,
    })

def month (request, year, month):
  month = date(int(year), int(month), 1)
  previous = month - timedelta(days=15)
  next = month + timedelta(days=45)

  return render_to_response('events/event_archive_month.html', {
    'month': month,
    'previous_month': previous,
    'next_month': next,
    })
