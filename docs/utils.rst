=====
Utils
=====

File
----
    niav/niav/utils.py

Class
-----

Niav Utilities.

Group here useful methods from various modules to avoid many import in tests.

.. code-block::

  get_random_integer(start, end)
      Return a random integer between start and end.

        start:  int. Start number.
        end:    int. End number.

        return: int. random number.

.. code-block::

  get_random_string(length=10)
      Return a random string made of ascii letters and digits.

        length: int. Expected string length. (default: 10)

        return: string. Random string.

.. code-block::

  json_dump(obj, ensure_ascii=False)
      Python object to Json format

.. code-block::

  json_load(obj_json)
      Json format to Python object

.. code-block::

  pprint(array)
      Pretty print a dict.

        array: dict. Dict to print.

.. code-block::

  sleep(seconds)
      Wait during x seconds

        seconds: int. Number of seconds to wait.

.. code-block::

  timestamp_now_js()
      Get a NOW timestamp in milliseconds

        return: float. Timestamp in milliseconds.

