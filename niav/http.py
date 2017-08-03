import requests
import logging

from niav.utils import Utils


class Http(object):
    """
        Requests wrapper.
        
        Add some helpers:
        - default headers
        - auto json loads
        - open files
        - cookies to dict
    """

    def __init__(self):
        self.handler = requests
        logging.getLogger("requests.packages.urllib3.connectionpool").setLevel(logging.WARNING)
        self.log = logging.getLogger("niav")
        self.env = None

    def __request(self, method, url, query_params=None, headers=None, files=None, data=None, json_opt=None, **kwargs):
        default_headers = {
            "Accept": "*/*",
            "Accept-Encoding": "identity, deflate, compress, gzip",
            "User-Agent": "Niav/0.x",
        }

        if query_params is None:
            query_params = {}

        if headers is not None:
            default_headers.update(headers)

        if files is not None:
            files = dict((key, open(filename, "rb")) for key, filename in files.items())

        method = method.upper()
        if method not in ["GET", "POST", "PUT"]:
            raise NameError("'%s' is not a supported HTTP method" % method)

        if self.env is not None:
            if self.env.get_unsafe("niav_http.disable_ssl_warning"):
                if self.env.get_unsafe("niav_http.disable_ssl_warning").lower() == "true":
                    import urllib3
                    urllib3.disable_warnings()

            if "verify" not in kwargs and self.env.get_unsafe("niav_http.verify"):
                value = self.env.get_unsafe("niav_http.verify")
                if value.lower() == "true":
                    value = True
                elif value.lower() == "false":
                    value = False
                self.set_kwargs(kwargs, "verify", value)

            if "cert" not in kwargs and self.env.get_unsafe("niav_http.cert_crt") and self.env.get_unsafe("niav_http.cert_key"):
                self.set_kwargs(kwargs, "cert", (self.env.get_unsafe("niav_http.cert_crt"), self.env.get_unsafe("niav_http.cert_key")))

        if method == "POST":
            response = self.handler.post(url,
                                         params=query_params,
                                         headers=default_headers,
                                         files=files,
                                         data=data,
                                         json=json_opt,
                                         **kwargs)
        elif method == "GET":
            response = self.handler.get(url, params=query_params, headers=default_headers, **kwargs)
        else:
            response = self.handler.put(url,
                                        params=query_params,
                                        headers=default_headers,
                                        files=files,
                                        data=data,
                                        json=json_opt,
                                        **kwargs)

        json = {}
        try:
            json = Utils.json_load(response.text)
        except Exception as e:
            pass

        cookies = requests.utils.dict_from_cookiejar(response.cookies)
        if not cookies:
            if "Set-Cookie" in response.headers:
                header_cookies = response.headers["Set-Cookie"]
                cookies = dict(p.split('=') for p in header_cookies.split('; '))

        r = HttpResponse()
        r.status_code = response.status_code
        r.headers = dict(response.headers)
        r.content = response.text
        r.json = json
        r.cookies = cookies
        r.response = response

        return r

    def get(self, url, query_params=None, headers=None, **kwargs):
        """
            Make an HTTP request using 'GET' method

            :param url: URL to reach
            :param query_params: Query params (default: None)
            :param headers: Custom headers to use (default: None)
            :type url: string
            :type query_params: dict
            :type headers: dict
            :return: status code (int), list of headers (dict), content (string), json (dict),
                     cookies (dict), response (requests Response)
            :rtype: HttpResponse
        """
        return self.__request("get", url, query_params, headers, **kwargs)

    def post(self, url, query_params=None, headers=None, files=None, data=None, json=None, **kwargs):
        """
            Make an HTTP request using 'POST' method

            :param url: URL to reach
            :param query_params: Query params (default: None)
            :param headers: Custom headers to use  (default: None)
            :param files: Files to upload  (default: None)
            :param data: Payload (default: None)
            :param json: Payload (automatically serialized by requests) (default: None)
            :type url: string
            :type query_params: dict
            :type headers: dict
            :type files: dict
            :type data: dict
            :type json: dict
            :return: status code (int), list of headers (dict), content (string), json (dict),
                     cookies (dict), response (requests Response)
            :rtype: HttpResponse
        """
        return self.__request("post", url, query_params, headers, files, data, json_opt=json, **kwargs)

    def put(self, url, query_params=None, headers=None, files=None, data=None, json=None, **kwargs):
        """
            Make an HTTP request using 'PUT' method

            :param url: URL to reach
            :param query_params: Query params (default: None)
            :param headers: Custom headers to use  (default: None)
            :param files: Files to upload  (default: None)
            :param data: Payload (default: None)
            :param json: Payload (automatically serialized by requests) (default: None)
            :type url: string
            :type query_params: dict
            :type headers: dict
            :type files: dict
            :type data: dict
            :type json: dict
            :return: status code (int), list of headers (dict), content (string), json (dict),
                     cookies (dict), response (requests Response)
            :rtype: HttpResponse
        """
        return self.__request("put", url, query_params, headers, files, data, json_opt=json, **kwargs)

    def set_env(self, env):
        self.env = env

    @classmethod
    def set_kwargs(cls, kwargs, name, value):
        if not isinstance(kwargs, dict):
            kwargs = {}
        kwargs[name] = value


class HttpResponse(object):
    """
        Requests Response wrapper.
    """
    def __init__(self):
        self._status_code = None
        self._headers = None
        self._content = None
        self._json = None
        self._cookies = None
        self._response = None

    @property
    def status_code(self):
        return self._status_code

    @status_code.setter
    def status_code(self, value):
        self._status_code = value

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, value):
        self._headers = value

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def json(self):
        return self._json

    @json.setter
    def json(self, value):
        self._json = value

    @property
    def cookies(self):
        return self._cookies

    @cookies.setter
    def cookies(self, value):
        self._cookies = value

    @property
    def response(self):
        return self._response

    @response.setter
    def response(self, value):
        self._response = value

