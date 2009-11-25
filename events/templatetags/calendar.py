# Template tag
from datetime import date, timedelta

from django import template
from agenda.events.models import Event

register = template.Library()

def get_last_day_of_month(year, month):
    if (month == 12):
        year += 1
        month = 1
    else:
        month += 1
    return date(year, month, 1) - timedelta(1)


def month_cal(event_list, year, month):
    first_day_of_month = date(year, month, 1)
    last_day_of_month = get_last_day_of_month(year, month)
    first_day_of_calendar = first_day_of_month - timedelta(first_day_of_month.isoweekday())
    last_day_of_calendar = last_day_of_month + timedelta(7 - last_day_of_month.isoweekday())
    today = date.today();

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

        if day.isoweekday() == 6:
            month_cal.append(week)
            week = []

        i += 1
        day += timedelta(1)

    return {'calendar': month_cal, 'headers': week_headers}

register.inclusion_tag('calendar.html')(month_cal)
