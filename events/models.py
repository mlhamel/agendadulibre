# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Region (models.Model):
  id = models.PositiveSmallIntegerField(primary_key=True)
  name = models.CharField (max_length=200)

  def __unicode__ (self):
    return self.name

class City (models.Model):
  class Meta:
    verbose_name_plural = "cities"
    ordering = ['name']

  name = models.CharField (max_length=200)
  region = models.ForeignKey(Region)
  latitude = models.FloatField ()
  longitude = models.FloatField ()

  def __unicode__ (self):
    return self.name

class Event (models.Model):
  title = models.CharField (max_length=200,
      verbose_name="titre",
      help_text="Décrivez en moins de 5 mots votre évènement, sans y indiquer le lieu, la ville ou la date.")
  description = models.TextField (
      verbose_name="Description",
      help_text="""Décrivez de la manière la plus complète possible votre évènement.
Les balises HTML autorisées sont <p>, <b>, <i>, <ul>, <ol>, <li>, <br/>, <a>. Merci d'utiliser ces balises pour formater la description de votre évènement.
Veillez à utiliser les balises <p> pour formater les paragraphes, et non la balise <br/>.""")
  url = models.URLField (
      verbose_name="site web",
      help_text="Lien direct vers une page donnant plus d'informations sur l'évènement (lieu précis, horaire précis, programme précis...)")
  start_time = models.DateTimeField (
      verbose_name="Début")
  end_time = models.DateTimeField (
      verbose_name="Fin")
  submission_time = models.DateTimeField (auto_now_add=True);
  updated_time = models.DateTimeField (auto_now=True);

  address = models.CharField (max_length=200,
      verbose_name="Addresse",
      help_text="Numéro de porte et nom de rue de l'endroit"
      )
  city = models.ForeignKey(City,
      verbose_name="Ville")
  latitude = models.FloatField (blank=True,default=0)
  longitude = models.FloatField (blank=True,default=0)

  contact = models.CharField (max_length=200,
      verbose_name="Personne ressource",
      help_text="Entrez le nom d'une personne que les visiteurs peuvent contacter pour plus d'information")
  contact_email = models.EmailField (max_length=200,
      verbose_name="Courriel",
      help_text="Entrez le courriel de la personne ressource")

  moderator = models.ForeignKey(User, blank=True, null=True, related_name="moderated_events")
  moderated = models.BooleanField (default=False)
  decision_time = models.DateTimeField (blank=True,null=True);

  def __unicode__ (self):
    return self.title

