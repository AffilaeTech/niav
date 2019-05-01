import os
import logging

from configparser import ConfigParser


class Env(object):
    """
        NIAV Environment
    """

    def __init__(self, caller=None):
        """
            Parse env.ini file(s):
                - from constructor
                - from NIAV_ENV environment variable

            :raises: IOError if none of the paths are valid 
        """
        self.log = logging.getLogger("niav")
        self.config = ConfigParser()
        config_files = []
        self.verbose = False
        self.tests_path = None

        if caller is not None:
            try:
                self.tests_path = os.path.split(caller)[0]

                auto_conf = os.path.join(self.tests_path, "env.ini")
                if os.path.exists(auto_conf):
                    config_files.append(auto_conf)

                auto_conf = os.path.join(self.tests_path, "local.ini")
                if os.path.exists(auto_conf):
                    config_files.append(auto_conf)
            except:
                pass

        conf = os.environ.get('NIAV_ENV')

        if conf:
            config_files = [filename.strip() for filename in conf.split(",")]

        if not config_files:
            raise TypeError("NIAV .ini not found")

        for conf_file in config_files:
            if not os.path.exists(conf_file):
                raise IOError("file missing: %s, path does not exists" % conf_file)
            else:
                self.config.read(conf_file)
                self.log.info("using environment: %s" % conf_file)

        log_level = self.get_unsafe("log.level") if self.get_unsafe("log.level") is not None else logging.INFO
        self.log.setLevel(log_level)

        self.verbose = self.get_unsafe("log.verbose") if self.get_unsafe("log.verbose") is not None else False

    def get(self, mixed_key):
        """
            Get key value from NIAV_ENV config file

            :param mixed_key: Section and key to read as "section.key"
            :type mixed_key: string
            :return: Value of "key" in "section" from ini file
            :rtype: string
            :raises: Exception if "Section" or "Key" does not exist
        """
        section, key = mixed_key.split(".")
        if section not in self.config.sections():
            raise KeyError("section '%s' does not exists" % section)
        elif key not in self.config.options(section):
            raise KeyError("key '%s' does not exists" % key)
        return self.config.get(section, key)

    def get_unsafe(self, mixed_key):
        """
            Get key value from NIAV_ENV env.ini file.
            This method doesn't raise exception.

            :param mixed_key: Section and key to read as "section.key"
            :type mixed_key: string
            :return: Value of "key" in "section" from ini file. None if key or value doesn't exist.
            :rtype: string
        """
        section, key = mixed_key.split(".")
        if section not in self.config.sections():
            if self.verbose is True:
                self.log.info("section '%s' not found" % section)
            return None
        elif key not in self.config.options(section):
            if self.verbose is True:
                self.log.info("key '%s' not found in section '%s'" % (key, section))
            return None
        return self.config.get(section, key)

    def get_int(self, mixed_key):
        """
            Get key value from NIAV_ENV env.ini file

            :param mixed_key: Section and key to read as "section.key"
            :type mixed_key: string
            :return: Value of "key" in "section" from ini file
            :rtype: int
            :raises: Exception if "Section" or "Key" does not exist
        """
        section, key = mixed_key.split(".")
        if section not in self.config.sections():
            raise KeyError("section '%s' does not exists" % section)
        elif key not in self.config.options(section):
            raise KeyError("key '%s' does not exists" % key)
        return self.config.getint(section, key)

    def get_int_unsafe(self, mixed_key):
        """
            Get key value from NIAV_ENV env.ini file.
            This method doesn't raise exception.

            :param mixed_key: section and key to read as "section.key"
            :type mixed_key: string
            :return: value of "key" in "section" from ini file. None if key or value doesn't exist.
            :rtype: int
        """
        section, key = mixed_key.split(".")
        if section not in self.config.sections():
            if self.verbose is True:
                self.log.info("section '%s' not found" % section)
            return None
        elif key not in self.config.options(section):
            if self.verbose is True:
                self.log.info("key '%s' not found in section '%s'" % (key, section))
            return None
        return self.config.getint(section, key)

    def get_tests_path(self):
        return self.tests_path
