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
from django.shortcuts import render_to_response, HttpResponseRedirect
from django.views.generic.simple import redirect_to, direct_to_template
from datetime import date

def index (request):
  today = date.today ()
  return redirect_to (request, url="/event/%d/%d/" % (today.year, today.month))


def construction(request):
  return render_to_response("construction.html", {
      })


def about(request):
  return direct_to_template(request, template='about.html')


def settings (request):
  return render_to_response('events/settings.html', {

      })
