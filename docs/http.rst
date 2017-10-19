====
Http
====

File
----
    niav/niav/http.py

Class
-----

Requests wrapper.

Add some helpers:

- default headers

- auto json loads

- open files

- cookies to dict

.. code-block::

  get(url, query_params=None, headers=None):
      Make an HTTP request using 'GET' method

        url:            string. URL to reach.
        query_params:   dict. Query params. (default: None)
        headers:        dict. Custom headers to use. (default: None)

        return:         HttpResponse.  status code (int), list of headers (dict), content (string),
               json (dict), cookies (dict), response (Requests Response)

.. code-block::

  post(url, query_params=None, headers=None, files=None, data=None, json=None):
      Make an HTTP request using 'POST' method

        url:            string. URL to reach.
        query_params:   dict. Query params. (default: None)
        headers:        dict. Custom headers to use. (default: None)
        files:          dict. Files to upload. (default: None)
        data:           dict. Payload. (default: None)
        json:           dict. Payload. (automatically serialized by requests) (default: None)

        return:         HttpResponse.  status code (int), list of headers (dict), content (string),
               json (dict), cookies (dict), response (Requests Response)

.. code-block::

  put(url, query_params=None, headers=None, files=None, data=None, json=None):
      Make an HTTP request using 'PUT' method

        url:            string. URL to reach.
        query_params:   dict. Query params. (default: None)
        headers:        dict. Custom headers to use. (default: None)
        files:          dict. Files to upload. (default: None)
        data:           dict. Payload. (default: None)
        json:           dict. Payload. (automatically serialized by requests) (default: None)

        return:         HttpResponse.  status code (int), list of headers (dict), content (string),
               json (dict), cookies (dict), response (Requests Response)

.. code-block::

  set_env(env):
      Set an Env instance.

If the env is set, http will automatically read the following conf in env.ini (and local.ini):

niav_http.disable_ssl_warning
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(True/False)
Disable ssl warning.

niav_http.verify
~~~~~~~~~~~~~~~~
(True/False)
Niav ignore verifying the SSL certificate if you set verify to False.

niav_http.cert_crt and niav_http.cert_key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

See: `Client side certificates <http://docs.python-requests.org/en/master/user/advanced/#client-side-certificates>`_.

Niav support only the couple crt/key.

ex:

.. code-block::

  [niav_http]
  disable_ssl_warning = True
  verify = True
  cert_crt = /etc/ssl/certs/client.crt
  cert_key = /etc/ssl/private/client.key


============
HttpResponse
============

File
----
    niav/niav/http.py

Class
-----

Requests Response wrapper.

.. code-block::

  status_code():
      Get the http status code.

        return: int.

.. code-block::

  headers():
      Get headers.

        return: dict.

.. code-block::

  content():
      Get text content.

        return: string.

.. code-block::

  json():
      Get json content (if content can be unserialized).

        return: dict.

.. code-block::

  cookies():
      Get cookies.

        return: dict.

.. code-block::

  response():
      Get Requests object Response.

        return: Response.
