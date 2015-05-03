Software stack
==============


Languages
---------

The Plat/al project uses:

* Python3.4
* Javascript (ES5)
* bash (not sh)
* GNU Make

Application components
----------------------

Plat/al v2's stack is split in two parts:

Backend
    Developed with Django, this component provides a REST-like API over
    the internal directory.

    The API is built upon django-rest-framework; see :doc:`the API documentation <api>` for details.

Frontend
    The user-facing website is a full javascript, single-page application.

    It fetches data from the API, renders it, handles HTML events,
    and sends updates to the backend.


Front-end development
---------------------

This project uses modern engineering methods for front-end development.

This means that:

* External libraries are loaded from NPM or from Bower
* The required versions are expressed in either ``package.json`` (for development and server-side dependencies)
  and ``bower.json`` (for "in-browser" dependencies, both JS and CSS)
* The build pipeline (concatenation, minification, optimization) might use Gulp

The build process includes:

1. Loading development dependencies from NPM through ``npm install``
2. Loading in-browser dependencies from Bower through ``bower install``
3. Running JS compilation from project code and libraries, through ``gulp build``


Cache busting
-------------

For bandwidth efficiency, all assets (JS, CSS, images) **SHOULD** be served with a long cache duration (i.e cache forever).
This is possible if JS/CSS/image filenames include a hash of their content (e.g. ``platal.a244de499.js``)

This is performed using ``gulp-rev`` as a last build step.


Components
----------

Backend
"""""""

The backend provides at least some features, including:

* The admin console
* A Rest-like API, used by dynamic parts of the website
* A simple ``selftest`` page, where admins can check that all features are working properly


Frontend
""""""""

The front-end is based on a full-javascript, single-page application.

It is based upon the following components:

* UI: React.js
* Event/rendering loop: Flux
* Ajax wrapper: *to be defined*
* Event management: *to be defined*


Request handling
""""""""""""""""

Using a split stack makes debug more complex; here is a short description of what happens:

A user hitting https://www.polytechnique.org/ receives a simple HTML document that:

* Declares where version-specific JS/CSS/... files should be loaded
* Declares where the API is located
* Starts rendering the DOM through React.js

In details, the request is handled as follows:

1. The HTTP server (might be Django) receives the request
2. It generates a static HTML page, including the related JS/CSS files and the URL to the API
3. The browser parses this HTML page, and loads the JS/CSS
4. The JS app sends a few queries to the API to fetch more information (e.g the user's data)
5. The JS app updates the DOM, triggering a HTML re-render
6. When the user provides input, the JS app reacts by querying the API for the requested data
7. Based on that new data, the JS app updates the DOM again, triggering another HTML rendering.


Remote services
---------------

The site enables a user to configure other services, e.g:

* Mailing lists
* Newsgroups
* Email redirection accounts

In order to provide an easily reusable platform,
those services should expose a standardized configuration interface,
using a simple HTTP/JSON API.

This ensures that all components can be upgraded without breaking the user configuration pages.
