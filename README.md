Shutdown: _A Django App To Shut Down Your Django App_
=====

This is a simple app that can be used to bring down a PyPE django project by
simply adding an entry to an oracle table.

Usage
=====

To include this app in your PyPE project, simply pull it into your project via svn:externals.

> path: extra/shutdown

> URL: https://github.com/UT-Austin-FIS/shutdown/tags/v1.1.2/shutdown

Setup
------

1. Add "shutdown" to your INSTALLED_APPS setting like this::

      ```python
            INSTALLED_APPS = (
                ...
                'shutdown',
            )
      ```

2. Add the shutdown middleware to your MIDDLEWARE_CLASSES setting like this::

      ```python
            MIDDLEWARE_CLASSES= (
                ...
                'shutdown.middleware.ShutdownMiddleware',
            )
      ```

3. Add an SHUTDOWN_CONTEXT object to your settings.py. This should be a class that carries the core of your page context logic. If not supplied, the UTDirectContext will be used, but you will need to supply the api key in your settings (eg: API_KEY = 'your_api_key')::

      ```python
         SHUTDOWN_CONTEXT = 'path.to.your.desired.context.object'
      ```

6. Run `python manage.py migrate` to create the shutdown models.


**NOTE**: 
_Since this app creates a new table, if your database design involves multiple users, you will need to go through the same process that you typically use to migrate a table and grant privileges._


How To Implement a Shutdown
---------------------------

Implementing a shutdown is relatively simple. You simply need to add a message entry to the SHUTDOWN_SHUTDOWN table, and all susequent requests to your application will automatically render the shutdown page with that message. Once you are ready to resume normal operations, you simply delete that record from the table.

How you add and remove the record is entirely up to you. You can edit the table directly using SQL Developer, or you could write a simple interface that allows your administrative users to add/remove a table entry, and implement shutdowns as they desire.

Releases
========

* v1.1.2 (2018/2/20)
  * Adding support for Django 1.11
  * Converted TemplateView to function view

* v1.1.1 (2015/11/16)
  * Adding support for Django 1.8, by calling .flatten() on context instances in get_context_data, to prevent RemovedInDjango110Warnings.

* v1.1.0 (2015/02/05)
  * Adding support for Django 1.7, including Django Migrations
  * Adding missing bracket in template
  * Renaming view class from `Shutdown` to `ShutdownView`
  * Adding `__version__` to module

* v1.0 (2014/05/29)
  * initial release with support for at least:
    * Python 2.6
    * Django 1.4
    * South 0.7.3
