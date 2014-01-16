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

from django.db import models

import tweepy

class AccountManager(models.Manager):
    def get_default(self):
        return Account.objects.get(default=True)


class Account (models.Model):
    class Meta:
      verbose_name = "Compte Twitter"

    name = models.CharField (max_length=200)
    consumer_key = models.CharField (max_length=200)
    consumer_secret = models.CharField (max_length=200)
    access_token = models.CharField (max_length=200)
    access_token_secret = models.CharField (max_length=200)
    default = models.NullBooleanField(unique=True)

    objects = AccountManager()

    def __unicode__ (self):
        return self.name

    @property
    def auth(self):
        try:
            return self.__auth
        except AttributeError:
            self.__auth = tweepy.auth.OAuthHandler(self.consumer_key, self.consumer_secret)
        else:
            self.auth.set_access_token(self.access_key, self.access_secret)
        return self.__auth

    def tweet(self, text):
        return tweepy.API(self.auth).update_status(text)
