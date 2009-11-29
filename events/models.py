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
from django.contrib.auth.models import User
from tagging.fields import TagField

class Region (models.Model):
  id = models.PositiveSmallIntegerField(primary_key=True)
  name = models.CharField (max_length=200)

  def __unicode__ (self):
    return self.name

class City (models.Model):
  class Meta:
    verbose_name = "ville"
    ordering = ['name']

  name = models.CharField (max_length=200)
  region = models.ForeignKey(Region)
  latitude = models.FloatField ()
  longitude = models.FloatField ()

  def __unicode__ (self):
    return self.name

class Event (models.Model):
  class Meta:
    verbose_name = "événement"

  SCOPE = (
      ('L', 'Locale'),
      ('N', 'Nationale'),
      ('I', 'Internationale'),
  )

  title = models.CharField (max_length=200,
      verbose_name="titre",
      help_text="Décrivez en moins de 5 mots votre événement, sans y indiquer le lieu, la ville ou la date.")
  description = models.TextField (
      verbose_name="Description",
      help_text="""Décrivez de la manière la plus complète possible votre événement.
Les balises HTML autorisées sont &lt;p&gt;, &lt;b&gt;, &lt;i&gt;, &lt;ul&gt;, &lt;ol&gt;, &lt;li&gt;, &lt;br/&gt;, &lt;a&gt;. Utilisez &lt;h3&gt; jusqu'à &lt;h5&gt; pour diviser votre texte au besoin. Merci d'utiliser ces balises pour formater la description de votre événement. <br/>
Veillez à utiliser les balises &lt;p&gt; pour formater les paragraphes, et non la balise &lt;br/&gt;.""")
  url = models.URLField (
      verbose_name="site web",
      help_text="Lien direct vers une page donnant plus d'informations sur l'événement (lieu précis, horaire précis, programme précis...)")
  tags = TagField (help_text="Une liste de mots séparés par un espace. Ne pas mettre de lieu dans les tags. <br/>Exemple: python django")
  start_time = models.DateTimeField (
      verbose_name="Début",
      help_text="AAAA-MM-JJ HH:MM (format 24 heures)")
  end_time = models.DateTimeField (
      verbose_name="Fin",
      help_text="AAAA-MM-JJ HH:MM (format 24 heures)")
  scope = models.CharField(max_length=1,
      choices=SCOPE,
      verbose_name="portée",
      default ='L',
      help_text="Indiquez si l'événement s'adresse à un publique local, national ou international.")

  submission_time = models.DateTimeField (auto_now_add=True);
  updated_time = models.DateTimeField (auto_now=True);

  venue = models.CharField (max_length=200,
      blank=True,
      verbose_name="Nom de l'endroit",
      help_text="Optionnel. Nom de l'endroit où se déroule l'événement. <br/>Exemple: Pub chez Moe"
      )
  address = models.CharField (max_length=200,
      verbose_name="Adresse",
      help_text="Numéro de porte et nom de rue de l'endroit, et le local"
      )
  city = models.ForeignKey(City,
      verbose_name="Ville")
  latitude = models.FloatField (blank=True,default=0)
  longitude = models.FloatField (blank=True,default=0)

  contact = models.CharField (max_length=200,
      verbose_name="Personne ressource",
      help_text="Entrez le nom d'une personne que les visiteurs peuvent contacter pour plus d'information")
  contact_email = models.EmailField (max_length=200,
      verbose_name="Courriel de cette personne",
      help_text="Entrez le courriel de la personne ressource")

  moderator = models.ForeignKey(User, blank=True, null=True, related_name="moderated_events")
  moderated = models.BooleanField (default=False)
  decision_time = models.DateTimeField (blank=True,null=True);

  submiter_email = models.EmailField (max_length=200,
      verbose_name="Votre courriel",
      help_text="Entrez votre courriel, vous serez responsable de cette entrée dans l'Agenda. Ce courriel ne sera pas rendu public. Un modérateur pourrait avoir besoin de vous contacter.")

  def __unicode__ (self):
    return self.title

  def get_absolute_url (self):
    return "/event/%i/" % self.id

