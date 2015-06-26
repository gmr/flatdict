.. FlatDict documentation master file, created by
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

FlatDict
========
|Version| |Downloads| |Status| |Coverage| |License|

**FlatDict** is a Python module for interacting with nested dicts as a single
level dict with delimited keys. :py:class:`~flatdict.FlatDict` supports Python 2.6+ and 3.2+.

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

    print flat['foo:bar:baz']

    flat['test:value:key'] = 10

    del flat['test']

    for key in flat:
        print key

    for values in flat.itervalues():
        print key

    print repr(flat.as_dict())

.. _docs:

Class Documentation
-------------------

.. automodule:: flatdict
    :members:
    :undoc-members:
    :inherited-members:

.. |Version| image:: https://badge.fury.io/py/flatdict.svg?
   :target: http://badge.fury.io/py/flatdict

.. |Status| image:: https://travis-ci.org/gmr/flatdict.svg?branch=master
   :target: https://travis-ci.org/gmr/flatdict

.. |Coverage| image:: https://codecov.io/github/gmr/flatdict/coverage.svg?branch=master
   :target: https://codecov.io/github/gmr/flatdict?branch=master

.. |Downloads| image:: https://pypip.in/d/flatdict/badge.svg?
   :target: https://pypi.python.org/pypi/flatdict

.. |License| image:: https://pypip.in/license/flatdict/badge.svg?
   :target: https://flatdict.readthedocs.org
