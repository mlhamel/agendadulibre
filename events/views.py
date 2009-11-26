from datetime import date, timedelta
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.http import HttpResponseNotFound
from events.forms import EventForm, RegionFilterForm
from events.models import Region
from agenda.events.feeds import UpcomingEventCalendarByRegion

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

def feed_list (request):

  region_list = Region.objects.all()

  return render_to_response('events/feeds.html', {
    'region_list': region_list,
    })

def calendar_region (request, region_id):
  try:
    region = Region.objects.get(pk=region_id)
  except Region.DoesNotExist:
    return HttpResponseNotFound ()
  callable = UpcomingEventCalendarByRegion (region)

  return callable (request)


def month (request, year, month):
  month = date(int(year), int(month), 1)
  previous = month - timedelta(days=15)
  next = month + timedelta(days=45)

  form = RegionFilterForm(request)

  region = None
  if request.method == 'GET':
    form = RegionFilterForm(request.GET)
    if form.is_valid():
      region = form.cleaned_data['region']
  else:
    form = RegionFilterForm()

  return render_to_response('events/event_archive_month.html', {
    'month': month,
    'previous_month': previous,
    'next_month': next,
    'form': form,
    'region': region,
    })
