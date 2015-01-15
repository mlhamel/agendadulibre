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
from django.utils.cache import add_never_cache_headers
from django.views.generic import TemplateView, RedirectView
from datetime import date


class IndexView(RedirectView):
    permanent = False

    def get_redirect_url(self, *args, **kwargs):
        today = date.today()
        return "/event/%d/%d/" % (today.year, today.month)

    def options(self, *args, **kwargs):
        response = super(IndexView, self).options(*args, **kwargs)
        add_never_cache_headers(response)
        return response


class AboutView(TemplateView):
    template_name = 'about.html'


class ConstructionView(TemplateView):
    template_name = "construction.html"


class SettingsView(TemplateView):
    template_name = "events/settings.html"
