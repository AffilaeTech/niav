import random
import string
import time
import json
import logging
import subprocess


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
        if isinstance(obj, str):
            self.log.info(res)
        else:
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

    @classmethod
    def execute_command(cls, command, shell=False, text=True, check=True, executable=None, capture_output=False, **kwargs):
        """
            Execute a command

            :param command: command.
            :type command: string if shell=True or list if shell=False
            :param shell: if shell is true, you pass a single string to the shell, else you pass a list of arguments
                            to the OS.
            :type shell: bool
            :param text: if text is true, a string will be returned. A byte sequence else.
            :type text: bool
            :param check: If check is true, and the process exits with a non-zero exit code, a CalledProcessError
                            exception will be raised.
            :type check: bool
            :param executable: executable to use to run the command. ie: '/bin/bash' (default: /bin/sh)
            :type executable: string
            :param capture_output: If capture_output is true, stdout and stderr will be captured
            :type capture_output: bool
            :return: exist status code
            :rtype: int
        """
        if executable is not None and "executable" not in kwargs:
            cls.set_kwargs(kwargs, "executable", executable)

        if capture_output is True and "capture_output" not in kwargs:
            cls.set_kwargs(kwargs, "stdout", subprocess.PIPE)
            cls.set_kwargs(kwargs, "stderr", subprocess.PIPE)

        response = subprocess.run(command, shell=shell, universal_newlines=text, check=check, **kwargs)
        final_response = {
            "args": response.args,
            "return_code": response.returncode,
            "stdout": response.stdout,
            "stderr": response.stderr}

        return final_response

    @classmethod
    def set_kwargs(cls, kwargs, name, value):
        if not isinstance(kwargs, dict):
            kwargs = {}
        kwargs[name] = value
