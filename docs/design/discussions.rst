Archived design discussions
===========================

For future reference, this document lists a few elements that led to the current
choice of technology, stack, ...


Front-end development
---------------------

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

