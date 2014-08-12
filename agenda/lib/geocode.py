# -*- coding: utf-8 -*-

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
