Contributing
============

Resources
---------

=============== ============================================================
*Source code*   https://github.com/Polytechnique-org/platal2
*Documentation* http://platal.readthedocs.org/
*Milestones*    https://github.com/Polytechnique-org/platal2/milestones
*Issues*        https://github.com/Polytechnique-org/platal2/issues
*Help*          ``#platal`` on chat.freenode.net
=============== ============================================================


Development process
-------------------

Dev
    * Bugfixes go directly on ``master``
    * Small features start with an issue describing the problem
    * Begin the patchset with a piece of design documentation (might be a comment in the file)
    * Big features *must* start through a design doc in the ``docs/`` folder
    * Don't forget :doc:`automated tests <testing>`
    * Always add a :doc:`changelog` entry

Deployment
    * Merge ``master`` into ``prod``
    * Add the release date to the ChangeLog
    * Bump version numbers on the ``prod`` branch
    * Tag that commit
    * Build the packages (``make dist``) from that tag
    * Merge back ``prod`` into ``master``

Hotfixes
    Things break after a release?

    - Add the fix on the ``prod`` branch
    - Merge back ``prod`` into ``master``


Coding guidelines
-----------------

A consistent codebase is important for readability.
The coding guidelines should be used to *improve* readability;
watch `this talk <https://www.youtube.com/watch?v=wf-BqAjZb8M>`_ for a few examples.


Philosophy: :pep:`The Zen of Python <20>`
    | Beautiful is better than ugly.
    | Explicit is better than implicit.
    |
    | Simple is better than complex.
    | Complex is better than complicated.
    |
    | Flat is better than nested.
    | Sparse is better than dense.
    | Readability counts.
    |
    | Special cases aren't special enough to break the rules.
    | Although practicality beats purity.
    |
    | Errors should never pass silently.
    | Unless explicitly silenced.
    |
    | In the face of ambiguity, refuse the temptation to guess.
    | There should be one -- and preferably only one -- obvious way to do it.
    | Although that way may not be obvious at first unless you're Dutch.
    |
    | Now is better than never.
    | Although never is often better than *right* now.
    |
    | If the implementation is hard to explain, it's a bad idea.
    | If the implementation is easy to explain, it may be a good idea.
    |
    | Namespaces are one honking great idea -- let's do more of those!


Python
    Use `Django's style guide <http://django.readthedocs.org/en/latest/internals/contributing/writing-code/coding-style.html>`_

Javascript
    Use `AirBnB's coding rules <https://github.com/airbnb/javascript/tree/master/es5>`_
