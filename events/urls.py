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

month_list_info = {
    "month_format": "%m",
    "date_field": "start_time",
    "allow_future": True,
    "allow_empty": True,
}

event_info = general_info
event_list_info = dict(general_info, **list_info)
event_list_month_info = dict(general_info, **month_list_info)



urlpatterns = patterns('',
    (r'^$', list_detail.object_list, event_list_info),
    (r'^(?P<object_id>\d+)/$', list_detail.object_detail, event_info),
    (r'^(?P<year>\d+)/(?P<month>\d+)/$', date_based.archive_month, event_list_month_info),
)

