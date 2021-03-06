====
File
====

File
----
    niav/niav/file.py

Class
-----

File utilities

.. code-block::

  delete_file(path)
      Delete specified file

        path:   string. Full path to file.

.. code-block::

  get_tmp_file(size=0)
      Create temporary file of specified size

        size:   int. Expected size of created file. (default: 0)

        return: string. Created file full path.

.. code-block::

  get_tmp_folder()
      Return a temp folder

        return: string. tmp folder path.

.. code-block::

  sha1_file(path)
      Calculate sha1 of specified file

        path:   string. Full path to file.

        return: string. file sha1.

.. code-block::
  file_to_base64(path)
      Encode file to base64

        path:   string. Full path to file

        return: string. File base64 string
