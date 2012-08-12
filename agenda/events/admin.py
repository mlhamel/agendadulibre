# -*- encoding:utf-8 -*-
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

from django.contrib import admin
from agenda.events.models import Event, City, Region
from datetime import datetime
from django.core.mail import mail_admins

def make_published(self, request, queryset):
    rows_updated = queryset.update(moderated=True,moderator=request.user)
    if rows_updated == 1:
        message_bit = u"1 événement a été "
    else:
        message_bit = u"%s événements ont été " % rows_updated
    self.message_user(request, u"%s publié." % message_bit)

make_published.short_description = u"Publier les événements choisis"

def make_unpublished(self, request, queryset):
    rows_updated = queryset.update(moderated=False,moderator=request.user)
    if rows_updated == 1:
        message_bit = u"1 événement a été "
    else:
        message_bit = u"%s événements ont été " % rows_updated
    self.message_user(request, u"%s non publié." % message_bit)

make_unpublished.short_description = u"Non publier les événements choisis"

class EventAdmin(admin.ModelAdmin):
    date_hierarchy = 'start_time'
    list_filter = ('moderated',)
    actions = [make_published,make_unpublished]

class CityAdmin(admin.ModelAdmin):
    list_filter = ('region',)
    list_display = ('name','region')
    pass

admin.site.register(Event, EventAdmin)
admin.site.register(Region)
admin.site.register(City, CityAdmin)
