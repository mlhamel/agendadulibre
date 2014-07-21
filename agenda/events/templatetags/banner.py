#
# Copyright (C) 2014 Mathieu Leduc-Hamel
#
# Author:  Mathieu Leduc-Hamel <marrakis@gmail.com>
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

from datetime import date

from django import template

from agenda.events.models import Event

register = template.Library()


def latest_banner():
    today = date.today()
    q = (Event.objects
         .filter(moderated=True)
         .filter(start_time__gte=today)
         .filter(spotlight=True)
         .order_by('-submission_time'))
    try:
        return {'banner_event': q[0]}
    except (Event.DoesNotExist, IndexError):
        return {'banner_event': None}
register.inclusion_tag('banner.html')(latest_banner)
