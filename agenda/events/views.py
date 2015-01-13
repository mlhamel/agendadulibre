# -*- encoding:utf-8 -*-
#
# Copyright (C) 2009 Novopia Solutions Inc.
#
# Author: Pierre-Luc Beaudoin <pierre-luc.beaudoin@novopia.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from datetime import date, timedelta
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.http import HttpResponseNotFound
from agenda.events.forms import EventForm, RegionFilterForm
from agenda.events.models import Region, Event
from agenda.events.feeds import UpcomingEventCalendarByRegion
from agenda.events.utils import mail_moderators
from django.db.models import Count
from django.conf import settings


def propose(request):
    form = EventForm(request)

    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            e = form.save()
            if settings.ENABLE_MAIL:
                msg = (u"Bonjour, \n\nLe nouvel évènement '" + e.title
                       + u"' a été soumis.  Pour le réviser, veuillez visiter\n")
                msg += u"http://www.agendadulibre.qc.ca/admin/events/event/%d/" % e.id
                msg += u"\n\nMerci,\n\nL'Agenda du libre du Québec"
                mail_moderators(u"Nouvel évènement en attente de modération",
                                msg)
            return HttpResponseRedirect('/event/new/thanks/')
    else:
        form = EventForm()

    return render_to_response('events/event_new.html', {
        'form': form,
    })


def region_cmp (a, b):
    return a['value'] - b['value']


def stats(request):
    total = (Event.objects
             .filter(moderated=True)
             .aggregate(Count('id'))['id__count'])
    total_to_moderate = (Event.objects
                         .filter(moderated=False)
                         .aggregate(Count('id'))['id__count'])

    region_list = []
    regions = Region.objects.all()
    for region in regions:
        region_list.append({
            'name': region.name,
            'value': (Event.objects
                      .filter(moderated=True,city__region=region)
                      .aggregate(Count('id'))['id__count'])
        })
    region_list.sort(region_cmp, reverse=True)

    return render_to_response('events/stats.html', {
        'region_list': region_list,
        'total': total,
        'total_to_moderate': total_to_moderate,
    })


def feed_list(request):
    region_list = Region.objects.all()

    return render_to_response('events/feeds.html', {
        'region_list': region_list,
    })


def calendar_region(request, region_id):
    try:
        region = Region.objects.get(pk=region_id)
    except Region.DoesNotExist:
        return HttpResponseNotFound()
    callable = UpcomingEventCalendarByRegion(region)
    return callable(request)


def month(request, year, month):
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
