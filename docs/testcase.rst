========
TestCase
========

File
----
    niav/niav/testcase.py

Class
-----

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

.. code-block::

  TestCase(*args, **kwargs)
      Create an instance of the class that will use the named test
      method when executed. Raises a ValueError if the instance does
      not have a method with the specified name.

.. code-block::

  assertDictionaryHasKey(dictionary, key)
      Check if a key is present in a dictionary

        dictionary: dict. Dictionary to consider.
        key:        string. Key to search.

.. code-block::

  assertDictionaryHasKeyIgnoringCase(dictionary, key)
      Check if a key (ignoring case) is present in a dictionary

        dictionary: dict. Dictionary to consider.
        key:        string. Key to search.

.. code-block::

  assertDictionaryHasNotKey(dictionary, key)
      Check if a key is not present in dictionary

        dictionary: dict. Dictionary to consider.
        key:        string. Key to search.

.. code-block::

  assertIsDictionary(value)
      Check if the value is a dictionary

.. code-block::

  assertIsInteger(value)
      Check if a value is an integer

.. code-block::

  assertIsList(value)
      Check if a value is a list

.. code-block::

  assertIsString(value)
      Check if the value is a string

.. code-block::

  assertIsTuple(value)
      Check if a value is a tuple

.. code-block::

  assertListHasValue(list, value)
      Check if a value is present at least once in a list

        list:   list. List to consider.
        value:  string. Expected value.

.. code-block::

  assertListLength(list, length)
      Check a list length

        list:   list. List to consider.
        length: int. Expected length.



Methods inherited from unittest.case.TestCase:

.. code-block::

  assertAlmostEqual(first, second, places=None, msg=None, delta=None)
      Fail if the two objects are unequal as determined by their
      difference rounded to the given number of decimal places
      (default 7) and comparing to zero, or by comparing that the
      between the two objects is more than the given delta.

      Note that decimal places (from zero) are usually not the same
      as significant digits (measured from the most significant digit).

      If the two objects compare equal then they will automatically
      compare almost equal.

.. code-block::

  assertCountEqual(first, second, msg=None)
      An unordered sequence comparison asserting that the same elements,
      regardless of order.  If the same element occurs more than once,
      it verifies that the elements occur the same number of times.

          self.assertEqual(Counter(list(first)),
                           Counter(list(second)))

       Example:
          - [0, 1, 1] and [1, 0, 1] compare equal.
          - [0, 0, 1] and [0, 1] compare unequal.

.. code-block::

  assertDictContainsSubset(subset, dictionary, msg=None)
      Checks whether dictionary is a superset of subset.

.. code-block::

  assertDictEqual(d1, d2, msg=None)

.. code-block::

  assertEqual(first, second, msg=None)
      Fail if the two objects are unequal as determined by the '=='
      operator.

.. code-block::

  assertFalse(expr, msg=None)
      Check that the expression is false.

.. code-block::

  assertGreater(a, b, msg=None)
      Just like self.assertTrue(a > b), but with a nicer default message.

.. code-block::

  assertGreaterEqual(a, b, msg=None)
      Just like self.assertTrue(a >= b), but with a nicer default message.

.. code-block::

  assertIn(member, container, msg=None)
      Just like self.assertTrue(a in b), but with a nicer default message.

.. code-block::

  assertIs(expr1, expr2, msg=None)
      Just like self.assertTrue(a is b), but with a nicer default message.

.. code-block::

  assertIsNone(obj, msg=None)
      Same as self.assertTrue(obj is None), with a nicer default message.

.. code-block::

  assertIsNot(expr1, expr2, msg=None)
      Just like self.assertTrue(a is not b), but with a nicer default message.

.. code-block::

  assertIsNotNone(obj, msg=None)
      Included for symmetry with assertIsNone.

.. code-block::

  assertLess(a, b, msg=None)
      Just like self.assertTrue(a < b), but with a nicer default message.

.. code-block::

  assertLessEqual(a, b, msg=None)
      Just like self.assertTrue(a <= b), but with a nicer default message.

.. code-block::

  assertListEqual(list1, list2, msg=None)
      A list-specific equality assertion.

      Args:
          list1: The first list to compare.
          list2: The second list to compare.
          msg: Optional message to use on failure instead of a list of
                  differences.

.. code-block::

  assertMultiLineEqual(first, second, msg=None)
      Assert that two multi-line strings are equal.

.. code-block::

  assertNotAlmostEqual(first, second, places=None, msg=None, delta=None)
      Fail if the two objects are equal as determined by their
      difference rounded to the given number of decimal places
      (default 7) and comparing to zero, or by comparing that the
      between the two objects is less than the given delta.

      Note that decimal places (from zero) are usually not the same
      as significant digits (measured from the most signficant digit).

      Objects that are equal automatically fail.

.. code-block::

  assertNotEqual(first, second, msg=None)
      Fail if the two objects are equal as determined by the '!='
      operator.

.. code-block::

  assertNotIn(member, container, msg=None)
      Just like self.assertTrue(a not in b), but with a nicer default message.

.. code-block::

  assertNotRegex(text, unexpected_regex, msg=None)
      Fail the test if the text matches the regular expression.

.. code-block::

  assertRegex(text, expected_regex, msg=None)
      Fail the test unless the text matches the regular expression.

.. code-block::

  assertSequenceEqual(seq1, seq2, msg=None, seq_type=None)
      An equality assertion for ordered sequences (like lists and tuples).

      For the purposes of this function, a valid ordered sequence type is one
      which can be indexed, has a length, and has an equality operator.

      Args:
          seq1: The first sequence to compare.
          seq2: The second sequence to compare.
          seq_type: The expected datatype of the sequences, or None if no
                  datatype should be enforced.
          msg: Optional message to use on failure instead of a list of
                  differences.

.. code-block::

  assertSetEqual(set1, set2, msg=None)
      A set-specific equality assertion.

      Args:
          set1: The first set to compare.
          set2: The second set to compare.
          msg: Optional message to use on failure instead of a list of
                  differences.

      assertSetEqual uses ducktyping to support different types of sets, and
      is optimized for sets specifically (parameters must support a
      difference method).

.. code-block::

  assertTrue(expr, msg=None)
      Check that the expression is true.

.. code-block::

  assertTupleEqual(tuple1, tuple2, msg=None)
      A tuple-specific equality assertion.

      Args:
          tuple1: The first tuple to compare.
          tuple2: The second tuple to compare.
          msg: Optional message to use on failure instead of a list of
                  differences.
