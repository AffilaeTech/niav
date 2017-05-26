====
http
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

    |  **get**(url, query_params=None, headers=None):
    |    Make an HTTP request using 'GET' method
    |
    |     url: string. URL to reach.
    |     query_params: dict. Query params. (default: None)
    |     headers: dict. Custom headers to use. (default: None)
    |
    |     return: HttpResponse.  status code (int), list of headers (dict), content (string),
    |               json (dict), cookies (dict), response (Requests Response)
    |
    |  **post**(url, query_params=None, headers=None, files=None, data=None, json=None):
    |    Make an HTTP request using 'POST' method
    |
    |     url: string. URL to reach.
    |     query_params: dict. Query params. (default: None)
    |     headers: dict. Custom headers to use. (default: None)
    |     files: dict. Files to upload. (default: None)
    |     data: dict. Payload. (default: None)
    |     json: dict. Payload. (automatically serialized by requests) (default: None)
    |
    |     return: HttpResponse.  status code (int), list of headers (dict), content (string),
    |               json (dict), cookies (dict), response (Requests Response)
    |
    |  **put**(url, query_params=None, headers=None, files=None, data=None, json=None):
    |    Make an HTTP request using 'PUT' method
    |
    |     url: string. URL to reach.
    |     query_params: dict. Query params. (default: None)
    |     headers: dict. Custom headers to use. (default: None)
    |     files: dict. Files to upload. (default: None)
    |     data: dict. Payload. (default: None)
    |     json: dict. Payload. (automatically serialized by requests) (default: None)
    |
    |     return: HttpResponse.  status code (int), list of headers (dict), content (string),
    |               json (dict), cookies (dict), response (Requests Response)


============
httpResponse
============

File
----
    niav/niav/http.py

Class
-----

Requests Response wrapper.

    |  **status_code**():
    |   Get the http status code.
    |
    |   return: int.
    |
    |  **headers**():
    |   Get headers.
    |
    |   return: dict.
    |
    |  **content**():
    |   Get text content.
    |
    |   return: string.
    |
    |  **json**():
    |   Get json content (if content can be unserialized).
    |
    |   return: dict.
    |
    |  **cookies**():
    |   Get cookies.
    |
    |   return: dict.
    |
    |  **response**():
    |   Get Requests object Response.
    |
    |   return: Response.





