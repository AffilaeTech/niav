import logging

from .env import Env
from .http import Http
from .utils import Utils
from .file import File


class Niav(object):

    def __init__(self, caller=None):
        self.log = logging.getLogger("niav")
        self._env = Env(caller=caller)
        self._http = Http()
        self._http.set_env(self._env)
        self._utils = Utils()
        self._file = File()

    @property
    def env(self):
        return self._env

    @env.setter
    def env(self, value):
        self._env = value

    @property
    def http(self):
        return self._http

    @http.setter
    def http(self, value):
        self._http = value

    @property
    def utils(self):
        return self._utils

    @utils.setter
    def utils(self, value):
        self._utils = value

    @property
    def file(self):
        return self._file

    @file.setter
    def file(self, value):
        self._file = value
