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

import requests
import simplejson

from unidecode import unidecode


class GoogleMapsGeocoder(object):
    url = ("http://maps.googleapis.com/maps/"
           "api/geocode/json?address=%(address)s&sensor=false")

    def geocode(self, address):
        """ Fuzzy address lookup.

        Rate limited to 2500 requests/day """
        try:
            vals = dict(address=unidecode(unicode(address)))
            response = requests.get(self.url % vals).json()
            try:
                results = response.get('results').pop()
            except IndexError:
                raise Exception("Can't decode %s" % unicode(address))
            location = results.get('geometry').get('location')
            return dict(latitude=location.get('lat'),
                        longitude=location.get('lng'))
        except simplejson.scanner.JSONDecodeError, e:
            if not self.ignore_exception:
                raise e
