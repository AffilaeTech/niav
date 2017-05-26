====
file
====

File
----
    niav/niav/file.py

Class
-----

File utilities

    |  **delete_file**(path)
    |      Delete specified file
    |
    |       path: string. Full path to file.
    |
    |  **get_tmp_file**(size=0)
    |      Create temporary file of specified size
    |
    |       size: int. Expected size of created file. (default: 0)
    |
    |      return: string. Created file full path.
    |
    |  **get_tmp_folder**()
    |      Return a temp folder
    |
    |       return: string. tmp folder path.
    |
    |  **sha1_file**(path)
    |      Calculate sha1 of specified file
    |
    |       path: string. Full path to file.
    |       return: string. file sha1.
