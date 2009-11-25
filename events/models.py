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
  name = models.CharField (max_length=200)
  region = models.ForeignKey(Region)
  latitude = models.FloatField ()
  longitude = models.FloatField ()

  def __unicode__ (self):
    return self.name + " (" + self.region.name + ")"

class Event (models.Model):
  title = models.CharField (max_length=200)
  description = models.TextField ()
  url = models.URLField ()
  start_time = models.DateTimeField ()
  end_time = models.DateTimeField ()
  submission_time = models.DateTimeField (auto_now_add=True);
  updated_time = models.DateTimeField (auto_now=True);

  address = models.CharField (max_length=200)
  city = models.ForeignKey(City)
  latitude = models.FloatField ()
  longitude = models.FloatField ()

  contact = models.CharField (max_length=200)
  contact_email = models.EmailField (max_length=200)

  submitter = models.ForeignKey(User, related_name="submitted_events")

  moderator = models.ForeignKey(User, blank=True, related_name="moderated_events")
  moderated = models.BooleanField (default=False)
  submitter = models.ForeignKey(User)
  decision_time = models.DateTimeField (blank=True);

  def __unicode__ (self):
    return self.title

