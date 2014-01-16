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
from django.views.generic.simple import direct_to_template
from django.conf import settings
from django.contrib import admin

import os

admin.autodiscover()

admin_media_path = os.path.join(os.path.dirname(admin.__file__), 'media')

urlpatterns = patterns('',
    (r'^e/', include('agenda.events.urls')),
    (r'^event/', include('agenda.events.urls')),
    (r'^twitter/', include('agenda.twitter.urls')),
    (r'^$', 'agenda.views.index'),
    (r'^about/$', 'agenda.views.about'),
    (r'^settings/$', 'agenda.views.settings'),

    (r'^login/$', 'django.contrib.auth.views.login'),

    (r'^admin/', include(admin.site.urls)),

    (r'^admin_media/(.*)', 'django.views.static.serve',
         {'document_root' : admin_media_path, 'show_indexes' : True}),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
)
