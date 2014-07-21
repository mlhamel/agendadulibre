Présentation
============

L'Agenda du libre du Québec est une copie conforme de l'agendadulibre.org
(France). Puisque ce dernier est disponible sous licence GPL,  la mise en place
 de ce clône a été plutôt rapide.  Plusieurs textes de la version québécoise
proviennent de la version française.

Dans les détails, la version québécoise est une réimplémentation en Django de
leur version en PHP. Ce changement technologique s'est avéré  nécessaire dû au
fait que la version de France n'a pas de séparation MVC, rendant difficile la
création d'une version avec des textes différents. Néanmoins, le principe de
fonctionnement est idéal et il a été reproduit avec minutie.

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
============

Pour installer l'agenda du libre du Québec vous n'avez suivre les différentes
étapes suivantes, toutefois, assurez-vous d'avoir Python 2.7.x:

    $ git clone https://github.com/mlhamel/agendadulibre.git
    $ cd agendadulibre
    $ python bootstrap.py
    $ bin/buildout

Les dépendances seront téléchargées et installées dans le répertoire courant.
Ensuite vous n'avez qui initialiser la base de données (SQLite en
développement):

    $ bin/django syncdb
    $ bin/django migrate

Et voilà, et pour lancer l'agenda:

    $ bin/django runserver

Vous n'avez qu'à ouvrir l'url suivante: http://127.0.0.1:8000 dans votre
navigateur !