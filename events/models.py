from django.db import models
from django.contrib.auth.models import User

class Region (models.Model):
  id = models.PositiveSmallIntegerField(primary_key=True)
  name = models.CharField (max_length=200)

class City (models.Model):
  name = models.CharField (max_length=200)
  region = models.ForeignKey(Region)

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

