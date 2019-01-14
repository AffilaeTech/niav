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

.. code-blocks::

  execute_command(cls, command, shell=False, text=True, check=True, executable=None, capture_output=False, **kwargs)
       Execute a command

         command:        string if shell=True or list if shell=False. The command to execute.
                           "ls -al" (shell=True). Executed through the shell (default: /bin/sh)
                           ["ls", "-al"] (shell=False). Executed by the OS
         shell:          bool (default: false). if shell is true, you pass a single string to the shell, else you pass a
                           list of arguments to the OS.
         text:           bool (default: true). if text is true, a string will be returned. A byte sequence else.
         check:          bool (default: true). If check is true, and the process exits with a non-zero exit code,
                           a CalledProcessError exception will be raised.
         executable:     string (default: None). executable to use to run the command. ie: "/bin/bash" (default: /bin/sh)
         capture_output: bool (default: False). If capture_output is true, stdout and stderr will be captured.

         return:         dict. args (list), return_code (int), stdout (string), stderr (string)
