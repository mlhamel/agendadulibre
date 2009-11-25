from datetime import date
from django.shortcuts import render_to_response

def month (request, year, month):
  month = date(int(year), int(month), 1)

  return render_to_response('events/event_archive_month.html', {'month': month})
