===
env
===

File
----
    niav/niav/env.py

Class
-----

NIAV Environment

.. code-block::

  Env(caller=None)
      Parse env.ini file(s):
          - from constructor
          - from NIAV_ENV environment variable

        raises:     IOError if none of the paths are valid

  get(mixed_key)
      Get key value from NIAV_ENV config file

        mixed_key:  string. Section and key to read as "section.key".

        return:     string. Value of "key" in "section" from ini file.

        raises:     Exception if "Section" or "Key" does not exist.

  get_int(mixed_key)
      Get key value from NIAV_ENV env.ini file

        mixed_key:  string. Section and key to read as "section.key".

        return:     int. Value of "key" in "section" from ini file.

        raises:     Exception if "Section" or "Key" does not exist.

  get_int_unsafe(mixed_key)
      Get key value from NIAV_ENV env.ini file.
      This method doesn't raise exception.

        mixed_key:  string. Section and key to read as "section.key".

        return:     int. Value of "key" in "section" from ini file. None if key or value doesn't exist.

  get_unsafe(mixed_key)
      Get key value from NIAV_ENV env.ini file.
      This method doesn't raise exception.

        mixed_key:  string. Section and key to read as "section.key".

        return:     string. Value of "key" in "section" from ini file. None if key or value doesn't exist.
