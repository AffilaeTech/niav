import unittest
import logging


class TestCase(unittest.IsolatedAsyncioTestCase):
    """
        Add useful asserts to API testing
        
        - assertIsDictionary
        - assertDictionaryHasKey
        - assertDictionaryHasNotKey
        - assertDictionaryHasKeyIgnoringCase
        - assertIsString
        - assertIsInteger
        - assertIsTuple
        - assertIsList
        - assertListLength
        - assertListHasValue
    """

    def __init__(self, *args, **kwargs):
        super(TestCase, self).__init__(*args, **kwargs)
        self.log = logging.getLogger("niav")

    def assertIsDictionary(self, value):
        """
            Check if the value is a dictionary
        """
        self.assertTrue(isinstance(value, dict), "%s %s" % (type(value), value))

    def assertDictionaryHasKey(self, dictionary, key):
        """
            Check if a key is present in a dictionary

            :param dictionary: Dictionary to consider
            :param key: Key to search
            :type dictionary: dict
            :type key: string
        """
        self.assertIsDictionary(dictionary)
        self.assertTrue(key in dictionary, dictionary)

    def assertDictionaryHasNotKey(self, dictionary, key):
        """
            Check if a key is not present in dictionary

            :param dictionary: Dictionary to consider
            :param key: Key to search
            :type dictionary: dict
            :type key: string
        """
        self.assertIsDictionary(dictionary)
        self.assertFalse(key in dictionary, dictionary)

    def assertDictionaryHasKeyIgnoringCase(self, dictionary, key):
        """
            Check if a key (ignoring case) is present in a dictionary

            :param dictionary: Dictionary to consider
            :param key: Key to search
            :type dictionary: dict
            :type key: string
        """
        self.assertIsDictionary(dictionary)

        for current_key in dictionary:
            if key.lower() == current_key.lower():
                self.assertTrue(True, dictionary)
                return current_key
        self.assertTrue(False, dictionary)

    def assertIsString(self, value):
        """
            Check if the value is a string
        """
        self.assertTrue(isinstance(value, str) or isinstance(value, bytes), "%s %s" % (type(value), value))

    def assertIsInteger(self, value):
        """
            Check if a value is an integer
        """
        self.assertTrue(isinstance(value, int), "%s %s" % (type(value), value))

    def assertIsTuple(self, value):
        """
            Check if a value is a tuple
        """
        self.assertTrue(isinstance(value, tuple), "%s %s" % (type(value), value))

    def assertIsList(self, value):
        """
            Check if a value is a list
        """
        self.assertTrue(isinstance(value, list), "%s %s" % (type(value), value))

    def assertListLength(self, llist, length):
        """
            Check a list length

            :param llist: List to consider
            :param length: Expected length
            :type llist: list
            :type length: integer
        """
        self.assertIsList(llist)
        self.assertEqual(len(llist), length, llist)

    def assertListHasValue(self, llist, value):
        """
            Check if a value is present at least once in a list

            :param llist: List to consider
            :param value: Expected value
            :type llist: list
            :type value: string
        """
        self.assertIsList(llist)
        self.assertNotEqual(len(list(filter(lambda x: x == value, llist))), 0, (llist, value))
