====
Niav
====

File
----
    niav/niav/niav.py

Class
-----

Main NIAV component.

It create automatically instance of:

 - env

 - http

 - file

 - utils


.. code-block::

  Niav(caller=None)
      If the test script create an instance of Niav with *caller=__file__*, Niav will search for a *env.ini* and
        *local.ini* at the same level as the test file. It send it to Env.

        caller: string. path.

        raises: IOError if none of the paths are valid

  properties:

 - env

 - http

 - file

 - utils

.. code-block::

  Example:

    self.niav = Niav(__file__)

    # read a conf
    protocol = self.niav.env.get("http.protocol")

    # request
    r = self.niav.http.get("example.com/user/1")

    # get a temp folder
    f = self.niav.file.get_tmp_folder()

    # get a random number
    n = self.niav.utils.get_random_integer(0, 50)
