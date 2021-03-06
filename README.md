Présentation
============

L'Agenda du libre du Québec est une copie conforme de l'agendadulibre.org
(France). Puisque ce dernier est disponible sous licence GPL, la mise en place
 de ce clône a été plutôt rapide. Plusieurs textes de la version québécoise
proviennent de la version française.

Dans les détails, la version québécoise est une réimplémentation en Django de
leur version en PHP. Ce changement technologique s'est avéré nécessaire dû au
fait que la version de France n'a pas de séparation MVC, rendant difficile la
création d'une version avec des textes différents. (Note: la version française 
a été réfaite en Ruby en 2014.) Néanmoins, le principe de fonctionnement est 
idéal et il a été reproduit avec minutie.

Cette version est disponible sous licence GNU Affero General Public License.
C'est une licence qui est plus restritive que la GNU General Public License
dû au fait qu'elle oblige les applications accessibles via le Web à rendre leur
 code source disponible. Le code source est disponible ici. Ce changement de
licence est possible puisque L'Agenda du libre du Québec ne contient aucune
ligne de code de l'original. Le logo est un mélange de l'icône Tango pour
applications de calendrier et de la fleur de lys du drapeau du Québec. Les
icônes proviennent également du projet Tango.

L'Agendu du libre du Québec est aujourd'hui maintenu et administré par
Mathieu Leduc-Hamel avec la collaboration, pour la modération, de
 Guillaume Prate et Fabián Rodriguez.

Installation
========

Pour installer l'Agenda du libre du Québec, vous n'avez qu'à suivre les différentes
étapes suivantes. (Prérequis: Python 2.7.x, git, sqlite3) :

    $ git clone https://github.com/mlhamel/agendadulibre.git
    $ cd agendadulibre
    $ python bootstrap.py
    $ bin/buildout

Les dépendances seront téléchargées et installées dans le répertoire courant.
Ensuite vous n'avez qui initialiser la base de données (SQLite en
développement):

    $ bin/django syncdb
    $ bin/django migrate
    $ sqlite3 agendadulibre < agenda/events/sql/region.sql
    $ sqlite3 agendadulibre < agenda/events/sql/city.sql
    
Et voilà, et pour lancer l'agenda:

    $ bin/django runserver

Vous n'avez qu'à ouvrir l'url suivante: http://127.0.0.1:8000 dans votre
navigateur !

Installation en production
===================

Pour installer l'Agenda du libre en production, on vous conseille de ne pas 
utiliser SQLite3 car ce n'est pas une base de données très robuste pour un 
site web multi-usager. Nous avons donc choisit MySQL afin de faire rouler 
l'agenda en production.

Pour installer l'agenda en production il suffit de spécifier à buildout 
d'utiliser la configuration de production. Le tout compilera localement une
version de nginx et de uwsgi qui serviront l'agenda.

Vous n'avez donc qu'à suivre les étapes suivantes:

    $ git clone https://github.com/mlhamel/agendadulibre.git
    $ cd agendadulibre
    $ python bootstrap.py
    $ bin/buildout -c production -vvv
    
Vous devez encore une fois initialiser la base de données:

    $ bin/django syncdb
    $ bin/django migrate
    $ mysql agendadulibre < agenda/events/sql/region.sql
    $ mysql agendadulibre < agenda/events/sql/city.sql
    
Ensuite, nous utilisons supervisor afin de faire rouler le tout:

    $ bin/supervisord
    
Vous pouvez toujours vous connecter à supervisor afin d'avoir plus de détails
sur les processus qui roulent:

    $ bin/supervisorctl
    
Vous n'avez qu'à ouvrir l'url suivante: http://127.0.0.1:8000 dans votre
navigateur !

