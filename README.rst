FlatDict
========

|Version| |Status| |Coverage|

``FlatDict`` is a dict object that allows for single level, delimited key/value
pair mapping of nested dictionaries. You can interact with FlatDict like a normal
dictionary and access child dicts as you normally would or with the composite
key.

Examples
--------

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

API
---

Documentation is available at https://flatdict.readthedocs.io

Installation
------------

.. code-block:: bash

    $ pip install flatdict

Example Use
-----------

.. code-block:: python

    import pprint

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

    for value in flat.itervalues():
        print(value)

    pprint.pprint(flat.as_dict())

    pprint.pprint(dict(flat))

    print(flat == flat.as_dict())

.. |Version| image:: https://img.shields.io/pypi/v/flatdict.svg?
   :target: http://badge.fury.io/py/flatdict

.. |Status| image:: https://img.shields.io/travis/gmr/flatdict.svg?
   :target: https://travis-ci.org/gmr/flatdict

.. |Coverage| image:: https://img.shields.io/codecov/c/github/gmr/flatdict.svg?
   :target: https://codecov.io/github/gmr/flatdict?branch=master
