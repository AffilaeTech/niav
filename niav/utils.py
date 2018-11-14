import random
import string
import time
import json
import logging

from pprint import pprint, pformat


class Utils(object):
    """
        Niav Utilities.
        
        Group here useful methods from various modules to avoid many import in tests.
    """

    def __init__(self):
        self.log = logging.getLogger("niav")

    @classmethod
    def pprint(cls, obj, **kwargs):
        """
            Pretty print a dict (printed only if an error is throw)

            :param obj: dict to print
            :type obj: dict
        """
        print("")
        pprint(obj, **kwargs)

    def plog(self, obj, **kwargs):
        """
            Print an object

        :param obj: obj to log
        :param kwargs:
        :return:
        """
        res = pformat(obj, **kwargs)
        self.log.info("\n" + res)

    @classmethod
    def get_random_string(cls, length=10):
        """
            Return a random string made of ascii letters and digits.

            :param length: Expected string length
            :type length: int (default: 10)
            :return: Random string
            :rtype: string
        """
        letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return "".join([random.choice(letters + string.digits) for _ in range(length)])

    @classmethod
    def get_random_integer(cls, start, end):
        """
            Return a random integer between start and end.
            
            :param start: Start number
            :param end: End number
            :type start: int
            :type end: int
            :return: Random number
            :rtype: int
        """
        return random.randint(start, end)

    @classmethod
    def timestamp_now_js(cls):
        """
            Get a NOW timestamp in milliseconds
            
            :return: Timestamp in milliseconds
            :rtype: float
        """
        return time.time()

    @classmethod
    def sleep(cls, seconds):
        """
            Wait during x seconds
            
            :param seconds: Number of seconds to wait
            :type seconds: int
        """
        time.sleep(seconds)

    @classmethod
    def json_dump(cls, obj, ensure_ascii=False):
        """
            Python object to Json format
        """
        return json.dumps(obj, ensure_ascii=ensure_ascii)

    @classmethod
    def json_load(cls, obj_json):
        """
            Json format to Python object
        """
        return json.loads(obj_json)
