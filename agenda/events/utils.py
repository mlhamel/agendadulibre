# -*- encoding:utf-8 -*-
#
# Copyright (C) 2014 Mathieu Leduc-Hamel
#
# Author: Mathieu Leduc-Hamel <mlhamel@mlhamel.org>
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
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import BadHeaderError
from django.http import HttpResponse


def mail_submitter(event):
    pass


def mail_moderators(title, message):
    moderators = User.objects.filter(is_staff=True).filter(is_active=True)
    to_emails = [x.get('email') for x in moderators.values('email')]
    from_email = settings.FROM_EMAIL

    if title and message and from_email:
        try:
            send_mail(title, message, from_email, to_emails)
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return True
    return False
