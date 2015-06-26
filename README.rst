==========
 FlatDict
==========

|Version| |Downloads| |Status| |Coverage| |License|

``FlatDict`` is a dict object that allows for single level, delimited key/value pair
mapping of nested dictionaries. You can interact with FlatDict like a normal
dictionary and access child dicts as you normally would or with the composited
key.

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

API
---

``FlatDict`` has the same methods as dict in Python 2.6. In addition, it has a
``FlatDict.as_dict`` method which will return a pure nested dictionary from a
``FlatDict`` value.

Documentation is available at http://flatdict.readthedocs.org

Installation
------------

.. code-block:: bash

    $ pip install flatdict

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

    print flat['foo:bar:baz']

    flat['test:value:key'] = 10

    del flat['test']

    for key in flat:
        print key

    for values in flat.itervalues():
        print key

    print repr(flat.as_dict())

.. |Version| image:: https://img.shields.io/pypi/v/flatdict.svg?
   :target: http://badge.fury.io/py/flatdict

.. |Status| image:: https://img.shields.io/travis/gmr/flatdict.svg?
   :target: https://travis-ci.org/gmr/flatdict

.. |Coverage| image:: https://img.shields.io/codecov/c/github/gmr/flatdict.svg?
   :target: https://codecov.io/github/gmr/flatdict?branch=master

.. |Downloads| image:: https://img.shields.io/pypi/dm/flatdict.svg?
   :target: https://pypi.python.org/pypi/flatdict

.. |License| image:: https://img.shields.io/pypi/l/flatdict.svg?
   :target: https://flatdict.readthedocs.org
