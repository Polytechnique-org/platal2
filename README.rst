.. image:: https://travis-ci.org/Polytechnique-org/platal2.svg?branch=master
    :target: https://travis-ci.org/Polytechnique-org/platal2
.. image:: https://coveralls.io/repos/Polytechnique-org/platal2/badge.svg?branch=master&service=github
    :target: https://coveralls.io/github/Polytechnique-org/platal2?branch=master

platal2
=======


This repository hosts the next generation of plat/al, Polytechnique.org's PLATform for ALumni.

It is intended as a brand new, clean redesign of the main site:

* A clean backend accessed through a REST API
* A new, full-browser UI built upon React.js (to be confirmed)


The final design should be built around the following components:

* A main SQL database
* A cache (likely Redis)
* A search engine (likely ElasticSearch)
* A Django-based backend, exposing an API through django-rest-framework
* A full UI, using Backbone.js, Flux and React.js


Code layout
-----------

* ``backend/`` contains the backend project
* ``ui/`` contains the JS parts
* ``docs/`` include the documentation, built using Sphinx.


Install
-------

For the API:
    * Install Python3.4
    * Create a virtualenv: ``pyvenv ~/dev/venvs/platal2``
    * Enter it: ``. ~/dev/venvs/platal2``
    * Install requirements: ``cd backend; make install-deps``
    * Adapt ``example_settings.ini`` into a ``local_settings.ini`` suitable to access the production database
    * Setup the Django part: ``./manage.py syncdb``
    * Start it up! ``./manage.py runserver``

For the UI:
    * Install nodejs
    * Enter the UI directory: ``cd ui``
    * Install the dependencies: ``make install-deps``
    * Compile the project: ``make build``
    * Run the UI: ``make runserver``
    * In order for the UI to be able to fetch data, open https://platal2-demo.polytechnique.org/auth/login/?next=/api/ and login there


License
-------

* The UI is distributed under a yet-to-be-defined license, likely GPLv3
* The API code is distributed under the AGPL license.
