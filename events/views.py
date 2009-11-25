from datetime import date, timedelta
from django.shortcuts import render_to_response

def month (request, year, month):
  month = date(int(year), int(month), 1)
  previous = month - timedelta(days=15)
  next = month + timedelta(days=45)

  return render_to_response('events/event_archive_month.html', {
    'month': month,
    'previous_month': previous,
    'next_month': next,
    })
