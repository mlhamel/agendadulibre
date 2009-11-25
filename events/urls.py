from django.conf.urls.defaults import *
from django.views.generic import list_detail
from django.views.generic import date_based
from agenda.events.models import Event

general_info = {
    "queryset" : Event.objects.filter(moderated=True),
    "template_object_name" : "event",
}

list_info = {
    "paginate_by": 25,
}

event_info = general_info
event_list_info = dict(general_info, **list_info)

urlpatterns = patterns('',
    (r'^$', list_detail.object_list, event_list_info),
    (r'^(?P<object_id>\d+)/$', list_detail.object_detail, event_info),
    (r'^(?P<year>\d+)/(?P<month>\d+)/$', 'events.views.month'),
)

