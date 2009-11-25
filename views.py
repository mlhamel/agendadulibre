from django.views.generic.simple import redirect_to
from datetime import date

def index (request):
  today = date.today ()
  return redirect_to (request, url="/event/%d/%d/" % (today.year, today.month))
