# -*- encoding:utf-8 -*-
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

from django.template.defaultfilters import stringfilter
from datetime import datetime, timedelta
from django import template
import locale

register = template.Library()

@register.filter
def event_time(start, end):
    today = datetime.today ()
    result = ""

    # Hack! get the correct user local from the request
    loc = locale.getlocale()
    locale.setlocale(locale.LC_ALL, 'fr_CA.UTF8')

    if start == today:
        result += "Aujourd'hui "
    else:
        result += "Le %s " % start.strftime ("%A %d %B %Y")

    if start.day == end.day and start.month == end.month and start.year == end.year:
        result += "de %s " % start.strftime ("%H:%M")
        result += "à %s " % end.strftime ("%H:%M")
    else:
        result += "à %s" % start.strftime ("%H:%M")
        result += "jusqu'au %s" % end.strftime ("%A %d %B %Y à %H:%M")

    locale.setlocale(locale.LC_ALL, loc)
    return result

