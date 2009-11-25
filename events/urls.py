from django.conf.urls.defaults import *
from django.views.generic import list_detail
from django.views.generic.simple import direct_to_template
from agenda.events.models import Event
from agenda.events.feeds import LatestEntries, UpcomingEntries, UpcomingEventCalendar


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
    'latest': LatestEntries,
    'upcoming': UpcomingEntries,
}


urlpatterns = patterns('',
    (r'^$', list_detail.object_list, event_list_info),
    (r'^new/$', 'events.views.propose'),
    (r'^new/thanks/$', direct_to_template, {'template': 'events/event_thanks.html'}),
    (r'^(?P<object_id>\d+)/$', list_detail.object_detail, event_info),
    (r'^(?P<year>\d+)/(?P<month>\d+)/$', 'events.views.month'),

    (r'^feeds/icalendar/$', UpcomingEventCalendar()),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed',
        {'feed_dict': feeds}),



)

