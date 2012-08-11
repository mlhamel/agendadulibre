#
# Copyright (C) 2009 Novopia Solutions Inc.
#
# Author: Pierre-Luc Beaudoin <pierre-luc.beaudoin@nov
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
# -----
# This file is derived from http://www.djangosnippets.org/snippets/129/
# A code snipped that comes without licence information

from datetime import date, timedelta

from django import template
from agenda.events.models import Event
from django.db.models import Q

register = template.Library()

def get_last_day_of_month(year, month):
    if (month == 12):
        year += 1
        month = 1
    else:
        month += 1
    return date(year, month, 1) - timedelta(1)


def month_cal(year, month, region = None):

    first_day_of_month = date(year, month, 1)
    last_day_of_month = get_last_day_of_month(year, month)
    first_day_of_calendar = first_day_of_month - timedelta(first_day_of_month.weekday()+1)
    last_day_of_calendar = last_day_of_month + timedelta(7 - last_day_of_month.weekday())
    print last_day_of_month.isoweekday()
    today = date.today();

    # Filter local events for given region, include national and international events
    if region != None:
      q = Q(city__region=region,scope="L") | Q(scope="I") | Q(scope="N")
    else:
      q = Q()

    event_list = Event.objects.filter (
        start_time__gte=first_day_of_calendar,
        end_time__lte=last_day_of_calendar,
        moderated=True).filter (q)

    month_cal = []
    week = []
    week_headers = []

    i = 0
    day = first_day_of_calendar
    while day <= last_day_of_calendar:
        if i < 7:
            week_headers.append(day)

        cal_day = {}
        cal_day['day'] = day
        cal_day['event'] = False

        day_events = []
        for event in event_list:
            if day >= event.start_time.date() and day <= event.end_time.date():
                day_events.append (event)

        cal_day['events'] = day_events

        cal_day['in_month'] = (day.month == month)
        cal_day['is_past'] = (day < today)
        cal_day['is_today'] = (day == today)

        week.append(cal_day)

        if day.weekday() == 5:
            month_cal.append(week)
            week = []

        i += 1
        day += timedelta(1)

    return {'calendar': month_cal, 'headers': week_headers, 'region': region}

register.inclusion_tag('calendar.html')(month_cal)
