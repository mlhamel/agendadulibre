# -*- encoding:utf-8 -*-
# Template tag
from django.template.defaultfilters import stringfilter
from datetime import datetime, timedelta
from django import template

register = template.Library()

@register.filter
def event_time(start, end):
    today = datetime.today ()
    result = ""

    if start == today:
        result += "aujourd'hui "
    else:
        result += "le %s " % start.strftime ("%A %d %B %Y")

    if start.day == end.day and start.month == end.month and start.year == end.year:
        result += "de %s " % start.strftime ("%H:%M")
        result += "à %s " % end.strftime ("%H:%M")
    else:
        result += "à %s" % start.strftime ("%H:%M")
        result += "jusqu'au %s" % end.strftime ("%A %d %B %Y à %H:%M")

    return result

