====
Niav
====

Niav Is Another Validator

------

.. image:: https://img.shields.io/badge/python-3.5%2B-blue.svg

``Niav`` is a lightweight framework that allows you to quickly write functional tests for your API.

It's based on ``Pytest`` and add generic helpers like:

- testcase (python unittest asserts + custom asserts)

- env (environment manager)

- http (get, post, ...)

- ssh (run a command and get result, send/get a file)

- file (create tmp file, sha1sum, delete, ...)

- ssh_tunnel (local port forwarding)

- utils (json, random, pretty print, ...)

And dedicated helpers:

- mongo (MongoDB connector with transparent ssh tunnel)

- more soon...

Niav imposes nothing. If you don't like a helper, for example *http*, you can import directly *requests* or *urllib3* directly in your tests. You can also create your own helpers.

------

An example of an API test (`nose <http://docs.pytest.org/en/latest/nose.html>`_ format):

.. code-block:: python

    # content of ~/tests/test_example.py

    from niav.testcase import TestCase
    from niav.niav import Niav
    from niav.helpers.mongo.mongo import Mongo

    class TestExample(TestCase):

        # called before test(s)
        def setUp(self):
            self.niav = Niav(__file__)
            self.url = "%s://%s:%s" % (self.niav.env.get("api.protocol"),
                                       self.niav.env.get("api.host"),
                                       self.niav.env.get("api.port"))

        def test_example(self):

            # get books
            url = "%s/api/v1.0/books" % self.url
            r = self.niav.http.get(url)
            self.assertEqual(r.status_code, 200)
            self.assertDictionaryHasKey(r.json, "books")
            self.assertIsList(r.json["books"])
            self.assertListLength(r.json["books"], 2)

            # r.json = {
            #       "books": [
            #           {
            #               "id": "58a43ac0e8face6d1b8b4567",
            #               "title": "The blue car"
            #           },
            #           {
            #               "id": "58a43a9660c41d06462c0bd0",
            #               "title": "The penguin"
            #           }
            #       ]
            #   }

            # post a new book
            payload = {
                "title": "A little mouse",
                "isbn": "654-5-2846-1826-5"
            }
            url = "%s/api/v1.0/book" % self.url
            r = self.niav.http.post(url, data=payload)
            self.assertEqual(r.status_code, 200)
            self.assertDictionaryHasKey(r.json, "book")
            self.assertEqual(r.json["book"]["title"], "A little mouse")

            new_book_id = r.json["book"]["id"]

            # r.json = {
            #       "book": {
            #           "id": "593bce93052499c655000c78",
            #           "title": "A little mouse"
            #       }
            #   }

            # Your API doesn't return "isbn" because it's used only in internal.
            # you can check it directly in database
            mongo = Mongo(self.env)
            self.mongo_client = mongo.connect()
            db = self.mongo_client.your_database
            book = db.books.find_one({"_id": mongo.object_id(new_book_id)})
            mongo.close()
            self.assertEqual(book["isbn"], "654-5-2846-1826-5")


Configurations
--------------

env.ini & local.ini
~~~~~~~~~~~~~~~~~~~

For the above example to work, you must create a configuration file: env.ini

.. code-block:: python

    # content of ~/tests/env.ini

    [log]
    level = INFO

    [api]
    protocol = http
    host = 10.0.3.15
    port = 4200

    [tunnel_ssh]
    host = 10.0.3.20
    local_port = 27017
    remote_port = 27017
    port_ssh = 22
    user = john
    password = 124565
    private_key =
    private_key_password =

    [mongo]
    host = 127.0.0.1
    port = 27017

If you pass ``__file__`` in the constructor of Niav() like in the example, Niav will automatically search for a *env.ini* at the same level as the test file.

In the same way, it will look if a file *local.ini* exist.
*local.ini* is for secret things, like passwords, but also for things that can change between you and your colleagues.
Just add *local.ini* in your *.gitignore*.

Niav read *env.ini* first, and overwrite or add configurations with *local.ini* content.

The other way to set environment is with NIAV_ENV:

.. code-block:: bash

    NIAV_ENV=/home/${USER}/tests/env.ini /home/${USER}/venv/niav/bin/pytest tests/test_example.py (from virtualenv)

    # with local.ini
    NIAV_ENV=/home/${USER}/tests/env.ini,/home/${USER}/tests/local.ini /home/${USER}/venv/niav/bin/pytest tests/test_example.py (from virtualenv)

If you don't need a ssh tunnel, just remove tunnel_ssh configurations or comment the host of tunnel_ssh.


pytest.ini
~~~~~~~~~~

You can configure pytest with the file `pytest.ini <https://docs.pytest.org/en/latest/customize.html#builtin-configuration-file-options>`_.

.. code-block:: python

    # content of ~/tests/pytest.ini

    [pytest]
    addopts = --tb=short    # shorter traceback format

    log_format = %(asctime)s %(levelname)-7.7s %(filename)-30.30s: %(message)s
    log_date_format = %Y-%m-%d %H:%M:%S

    log_cli = True
    log_cli_level = INFO


Running tests
-------------

.. code-block:: bash

    # running a test (with env.ini/local.ini auto discovery)
    export PYTHONPATH=$PYTHONPATH:/home/${USER}/code/niav/; /home/${USER}/venv/niav/bin/pytest tests/functional_tests/test_example.py

    # running a test (without environment auto discovery)
    export PYTHONPATH=$PYTHONPATH:/home/${USER}/code/niav/; NIAV_ENV=/home/${USER}/tests/env.ini,/home/${USER}/tests/local.ini /home/${USER}/venv/niav/bin/pytest tests/functional_tests/test_example.py

To avoid having to give the PYTHONPATH of Niav, add it to your bash *.profile* or whatever, depending on your favorite shell.

.. code-block:: bash

    # running a test (with env.ini/local.ini auto discovery)
    /home/${USER}/venv/niav/bin/pytest tests/functional_tests/test_example.py

    # running all tests (with env.ini/local.ini auto discovery)
    /home/${USER}/venv/niav/bin/pytest tests/functional_tests/

    # running a test (without environment auto discovery)
    NIAV_ENV=/home/${USER}/tests/env.ini,/home/${USER}/tests/local.ini /home/${USER}/venv/niav/bin/pytest tests/functional_tests/test_example.py


Starting
--------

Copy / paste the *tests* folder from ``niav`` to your project.

Suggestion for use:

.. code-block::

    niav/
    ├── docs/
    │   └── some_docs
    ├── niav/
    │   ├── helpers/                ┌
    │   │   ├── mongo/              │   public helpers
    │   │   │   └── mongo.py        ┤
    │   │   └── mysql/              │
    │   │       └── mysql.py        └
    │   ├── env.py
    │   ├── file.py
    │   ├── http.py
    │   └── ...
    └── tests/                       ┌
        └── functional_tests/        │
            ├── helpers/             │
            │   └── template/        │  Template folder
            │       └── template.py  ┤
            ├── env.ini              │  Just copy it in your project
            ├── local.ini            │
            ├── pytest.ini           │
            └── test_template.py     └

    your_project_01/
    ├── docs/
    │   └── some_docs
    ├── main_code/
    │   └── ...
    └── tests/
        └── functional_tests/         ┌
            ├── helpers/              ┤  No need of private helpers in this project
            ├── env.ini               └
            ├── local.ini
            ├── pytest.ini
            ├── test_feature_01.py
            └── test_feature_02.py

    your_project_02/
    ├── docs/
    │   └── some_docs
    ├── main_code/
    │   └── ...
    └── tests/
        └── functional_tests/         ┌
            ├── helpers/              │  Private helpers. It can be a wrapper around http public helper to
            │   └── your_api/         ┤  add specific headers like "api_key", "token", ...
            │       └── your_api.py   │  Or a custom protocol manager/validator, etc...
            ├── env.ini               └
            ├── local.ini
            ├── pytest.ini
            ├── test_feature_01.py
            ├── test_feature_02.py
            └── ...


Documentation
-------------

Installation
~~~~~~~~~~~~

Please read `INSTALL <https://github.com/AffilaeTech/niav/blob/master/INSTALL.rst>`_.


Reference
~~~~~~~~~

Consult the `documentation <https://github.com/AffilaeTech/niav/blob/master/docs/index.rst>`_ for API reference.


Changelog
~~~~~~~~~

See `CHANGELOG <https://github.com/AffilaeTech/niav/blob/master/CHANGELOG.rst>`_ for fixes and enhancements of each version.


License
~~~~~~~

Copyright Frédéric Dogimont, 2017.

Distributed under the terms of the `MIT <https://github.com/AffilaeTech/niav/blob/master/LICENSE.rst>`_ license, Niav is free and open source software.
