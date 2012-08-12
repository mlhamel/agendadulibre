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

from django.conf.urls.defaults import *
from django.views.generic import list_detail
from django.views.generic.simple import direct_to_template
from agenda.events.models import Event
from agenda.events.feeds import (LatestEntries,
                                 UpcomingEntries,
                                 UpcomingEventCalendar,
                                 LatestEntriesByRegion,
                                 UpcomingEntriesByRegion,
                                 UpcomingEventCalendarByRegion)


general_info = {
    "queryset" : Event.objects.filter(moderated=True),
    "template_object_name" : "event",
}

list_info = {
    "paginate_by": 25,
}

event_info = general_info
event_list_info = dict(general_info, **list_info)

feeds = {
    'latest': LatestEntries(),
    'upcoming': UpcomingEntries(),
    'latest_region': LatestEntriesByRegion(),
    'upcoming_region': UpcomingEntriesByRegion(),
}


urlpatterns = patterns('',
    (r'^$', list_detail.object_list, event_list_info),
    (r'^new/$', 'agenda.events.views.propose'),
    (r'^new/thanks/$', direct_to_template, {'template': 'events/event_thanks.html'}),

    (r'^(?P<object_id>\d+)/$', list_detail.object_detail, event_info),
    url(r'^(?P<year>\d+)/(?P<month>\d+)/$', 'agenda.events.views.month', name="month_view"),

    (r'^stats/$', 'agenda.events.views.stats'),

    (r'^feeds/$', 'agenda.events.views.feed_list'),
    (r'^feeds/latest/$', LatestEntries()),
    (r'^feeds/upcoming/$', UpcomingEntries()),
    (r'^feeds/latest_region/(?P<region_id>\d+)/$', LatestEntriesByRegion()),
    (r'^feeds/upcoming_region/(?P<region_id>\d+)/$', UpcomingEntriesByRegion()),

    (r'^calendar/$', UpcomingEventCalendar()),
    (r'^calendar_region/(?P<region_id>\d+)/$', 'agenda.events.views.calendar_region'),

)
