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

from agenda.views import AboutView, IndexView, SettingsView
from django.views.generic import TemplateView
from django.conf.urls import url, include, patterns
from django.conf import settings
from django.contrib import admin

import os

admin.autodiscover()


admin_media_path = os.path.join(os.path.dirname(admin.__file__), 'media')


class View404(TemplateView):
    template_name = '404.html'


class View500(TemplateView):
    template_name = '500.html'


urlpatterns = patterns('',
    (r'^e/', include('agenda.events.urls')),
    (r'^event/', include('agenda.events.urls')),
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^about/$', AboutView.as_view(), name="about"),
    (r'^settings/$', SettingsView.as_view()),
    (r'^i18n/', include('django.conf.urls.i18n')),

    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', 'django.contrib.auth.views.logout'),

    (r'^admin/', include(admin.site.urls)),

    (r'^admin_media/(.*)', 'django.views.static.serve',
     {'document_root': admin_media_path, 'show_indexes' : True}),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
     {'document_root': settings.MEDIA_ROOT}),
)
