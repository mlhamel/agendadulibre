# -*- encoding:utf-8 -*-

from datetime import date, timedelta
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.http import HttpResponseNotFound
from events.forms import EventForm, RegionFilterForm
from events.models import Region, Event
from agenda.events.feeds import UpcomingEventCalendarByRegion
from django.db.models import Count
from django.core.mail import mail_admins


def propose (request):
  form = EventForm (request)

  if request.method == 'POST':
    form = EventForm(request.POST)
    if form.is_valid():
      e = form.save()
      msg = u"Bonjour, \n\nLe nouvel évènement '" + e.title + u"' a été soumis.  Pour le réviser, veuillez visiter\n"
      msg += u"http://www.agendadulibre.qc.ca/admin/events/event/%d/" % e.id
      msg += u"\n\nMerci,\n\nL'Agenda du libre du Québec"
      mail_admins (u"Nouvel évènement en attente de modération", msg)
      return HttpResponseRedirect('/event/new/thanks/')
  else:
    form = EventForm()

  return render_to_response('events/event_new.html', {
    'form': form,
    })


def stats (request):
  total = Event.objects.filter(moderated=True).aggregate(Count('id'))['id__count']
  total_to_moderate = Event.objects.filter(moderated=False).aggregate(Count('id'))['id__count']

  region_list = []
  regions = Region.objects.all()
  for region in regions:
     region_list.append ({
       'name': region.name,
       'value': Event.objects.filter(moderated=True,city__region=region).aggregate(Count('id'))['id__count']
       })

  return render_to_response('events/stats.html', {
    'region_list': region_list,
    'total': total,
    'total_to_moderate': total_to_moderate,
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
