# -*- encoding:utf-8 -*-
#
# Copyright (C) 2014 Mathieu Leduc-Hamel
#
# Author: Mathieu Leduc-Hamel <marrakis@gmail.com>
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

from django.core.management.base import BaseCommand, CommandError

from agenda.events.models import Event


class Command(BaseCommand):
    help = 'Send the tweet corresponding to a specific event'

    def add_arguments(self, parser):
        parser.add_argument('event_id', nargs='+', type=int)

    def handle(self, event_id, *args, **options):
        try:
            event = Event.objects.get(pk=event_id)
        except Event.DoesNotExist:
            raise CommandError('Event "%s" does not exist' % event_id)
        event.tweet()
        self.stdout.write('Successfully tweet "%s"' % event_id)
