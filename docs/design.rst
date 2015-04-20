Project design
==============


Stack
-----

Plat/al v2's stack has not yet been defined.

A few options are:

* Backend in Django, front-end using React.js and Flux
* Backend in Django, front-end in Django with bits of React.js

A modern front-end stack is required for:

* A quick, dynamic search module
* An ergonomic profile edition page


Front-end development
"""""""""""""""""""""

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
"""""""""""""

For bandwidth efficiency, all assets (JS, CSS, images) **SHOULD** be served with a long cache duration (i.e cache forever).
This is possible if JS/CSS/image filenames include a hash of their content (e.g. ``platal.a244de499.js``)

Depending on the chosen stack, that step is performed differently:

* With a full-JS frontend, this happens with ``gulp-rev`` as a last build step
* With a Django-frontend containing JS, this step is performed by Django's ``staticfiles`` system.


Backend
"""""""

Whichever stack gets chosen for the front-end (e.g "rendering HTML in the browser),
a traditional backend will run, based on Django.

It provides at least some features, including:

* The admin console
* A Rest-like API, used by dynamic parts of the website
* A simple ``selftest`` page, where admins can check that all features are working properly


Frontend
""""""""

Two approaches are possible for frontend development:

* All pages are rendered through Django templates, with some dynamic JS code for some pages
* Django only serves the API, all pages are rendered in the browser in JS


Django templates
''''''''''''''''

With this approach, a user's request to https://www.polytechnique.org/ is handled as follows:

1. The Django server receives the request
2. It finds the correct ``View`` through its routing rules
3. The ``View`` builds a context, chooses the HTML template,
   and provides both to the template rendering engine
4. Django sends back the rendered HTML template to the browser
5. The browser parses the HTML and presents

If the page is dynamic (e.g search, profile):

6. The browser loads the related Javascript files
7. The JS stack generates a HTML DOM section based on its state and (optional) API queries
8. When the user provides input, the JS stack queries the API
9. Based on the new data, the JS stack updates the DOM, triggering a HTML re-render



Pros
    - Closer to plat/al 1 design
    - Easy to write a simple page
    - The first page loads faster
Cons
    - Complex handling of mixups between Django HTML templates and React HTML templates
    - Behavior of the pages is split between two codebases
    - Each page loads the whole skeleton


React.js rendering
''''''''''''''''''

With this approach, a user hitting https://www.polytechnique.org/ receives a simple HTML document that:

* Declares where version-specific JS/CSS/... files should be loaded
* Declares where the API is located
* Starts rendering the DOM through React.js

In details, the request is handled as follows:

1. The Django (or Express) server receives the request
2. It generates a static HTML page, including the related JS/CSS files and the URL to the API
3. The browser parses this HTML page, and loads the JS/CSS
4. The JS app sends a few queries to the API to fetch more information (e.g the user's data)
5. The JS app updates the DOM, triggering a HTML re-render
6. When the user provides input, the JS app reacts by querying the API for the requested data
7. Based on that new data, the JS app updates the DOM again, triggering another HTML rendering.


On subsequent pages, only new *data* is loaded; the whole codebase was loaded along the first page.

Pros
    - Clean split of roles: Django provides the data, React provides the UI
    - A single codebase for the whole UI
    - Pages feel more dynamic
    - Comes with great browser-based testing tools
    - Rate-limiting searches is easier, since it's a single entrypoint in the API
Cons
    - Unusual paradigm and language
    - Adding a new page might be more complex (to be confirmed)
    - The whole app must load before the user sees anything (can be avoided with e.g http://skitjs.com)


Remote services
"""""""""""""""

The site enables a user to configure other services, e.g:

* Mailing lists
* Newsgroups
* Email redirection accounts

In order to provide an easily reusable platform,
those services should expose a standardized configuration interface,
using a simple HTTP/JSON API.

This ensures that all components can be upgraded without breaking the user configuration pages.



Migration from plat/al 1
------------------------

For a smooth transition from the first version of plat/al,
some rules are required.


Coexistence
    * The new site **MUST** reuse most URLs from the old site
    * The Apache config can be used to switch sets of URLs to the new site

Database
    * The old MySQL database will be kept as the main storage engine
    * An additional database can be used for specific needs of the new stack
    * Old tables can be altered (e.g adding an ``auto_increment`` field) for greater compatibility

Authentication
    * Users **SHALL** authenticate only once during a session, even when switching versions
    * The password (for strong authentication with sensitive tasks) **MAY** be required twice,
      as few pages require this for common usage
    * Option 1: Use ``authgroupex`` from the new site to the old
    * Option 2: The new site reads the PHP sessions — but this might break logout

Design
    * Skin choice isn't available on the new site
    * Enforce the ``NewDefault`` skin for the old site once finished
    * Make sure the menu / header / footer have the same look between both sites


