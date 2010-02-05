#!/usr/bin/python
# -*- encoding: utf-8 -*-

# Use this script to submit a new event to L'Agenda
# This version of the script will submit an event for the next thursday

import urllib
import urllib2
import datetime

# Compute the date of the next event

day = 3 # thursday
next_date = datetime.date.today()
add = 0

if next_date.weekday() > day:
  add = 7 - next_date.weekday() + day
elif next_date.weekday() < day:
  add = day - next_date.weekday()
next_date += datetime.timedelta (days = add)

print "Soumettre un événement pour le ", next_date, "?"
raw_input("Appuyez sur Entrée pour poursuivre...")

url = 'http://www.agendadulibre.qc.ca/event/new/'

# Build HTML Form values
values = {
    'title' : 'L\'heure Ubuntu',
    'description' : """
        <p>L'Ubuntu Hour est bien simple</p>
        <ul>
          <li>Trouver un endroit avec une connectivité Internet près d'où vous
          travaillez ou habitez </li>
          <li>Portez quelque chose qui comporte le logo d'Ubuntu ou apportez votre
          ordinateur avec un collant Ubuntu</li>
          <li>Les participants doivent respecter le <a
          href="http://www.ubuntu.com/community/conduct">Ubuntu Code of Conduct</a></li>
          <li>Il peut y avoir un Ubuntu Hour partout, n'importe quand!</li>
        </ul>""",
    'url' : 'http://wiki.ubuntu.com/Hour',
    'tags' : 'ubuntu hour',

    'scope' : 'L', # L = Local, N = National, I = International
    'venue' : 'Café Suprême',
    'address' : '4190 Boulevard St-Laurent ',
    'city' : '1', # 1 = Montréal

    'contact' : 'Fabián Rodríguez',
    'contact_email' : 'magicfab@ubuntu.com',
    'submiter_email' : 'magicfab@ubuntu.com',

    'start_time_0_day' : str(next_date.day),
    'start_time_0_month' : str(next_date.month),
    'start_time_0_year' : str(next_date.year),
    'start_time_1_hour' : '12',
    'start_time_1_minute' : '00',

    'end_time_0_day' : str(next_date.day),
    'end_time_0_month' : str(next_date.month),
    'end_time_0_year' : str(next_date.year),
    'end_time_1_hour' : '13',
    'end_time_1_minute' : '00',
    }


# Submit the values

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
try:
  response = urllib2.urlopen(req)
  print "Événement soumit."
except URLError, e:
  if e.code == 404:
    print "Mauvaise addresse de soumission"
  elif e.code == 500:
    print "Erreur coté serveur"
