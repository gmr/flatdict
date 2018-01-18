.. FlatDict documentation master file, created by
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

FlatDict
========
|Version| |Status| |Coverage| |License|

**FlatDict** is a Python module for interacting with nested dicts as a single
level dict with delimited keys. FlatDict supports Python 2.7+ and 3.4+.

Jump to :ref:`installation`, :ref:`example`, :ref:`docs`, or :ref:`license`.

*For example:*

.. code-block:: python

    foo = {'foo': {'bar': 'baz', 'qux': 'corge'}}

*is represented as:*

.. code-block:: python

    {'foo:bar': 'baz',
     'foo:qux': 'corge'}

*And can still be accessed as:*

.. code-block:: python

    foo['foo']['bar']

*and*

.. code-block:: python

    foo['foo:bar']

Additionally, lists and tuples are also converted into dicts using enumerate().

*For example:*

.. code-block:: python

    d = {'list': ['a', 'b', 'c',]}

*Will be flattened as follows:*

.. code-block:: python

    flat = {'list:0': 'a', 'list:1': 'b', 'list:2': 'c'}

.. _installation:

Installation
------------

.. code-block:: bash

    $ pip install flatdict

.. _example:

Example Use
-----------

.. code-block:: python

    import flatdict

    values = {'foo': {'bar': {'baz': 0,
                              'qux': 1,
                              'corge': 2},
                      'grault': {'baz': 3,
                                 'qux': 4,
                                 'corge': 5}},
              'garply': {'foo': 0, 'bar': 1, 'baz': 2, 'qux': {'corge': 3}}}

    flat = flatdict.FlatDict(values)

    print(flat['foo:bar:baz'])

    flat['test:value:key'] = 10

    del flat['test']

    for key in flat:
        print(key)

    for values in flat.itervalues():
        print(value)

    print(repr(flat.as_dict()))

    print(flat == flat.as_dict())

.. _docs:

Class Documentation
-------------------

.. automodule:: flatdict
    :members:
    :undoc-members:
    :inherited-members:

.. |Version| image:: https://img.shields.io/pypi/v/flatdict.svg?
   :target: http://badge.fury.io/py/flatdict

.. |Status| image:: https://img.shields.io/travis/gmr/flatdict.svg?
   :target: https://travis-ci.org/gmr/flatdict

.. |Coverage| image:: https://img.shields.io/codecov/c/github/gmr/flatdict.svg?
   :target: https://codecov.io/github/gmr/flatdict?branch=master

.. |License| image:: https://img.shields.io/pypi/l/flatdict.svg?
   :target: https://flatdict.readthedocs.io
