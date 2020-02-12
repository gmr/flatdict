FlatDict
========
|Version| |Status| |Coverage| |License|

``flatdict`` is a Python module for interacting with nested dicts as a single
level dict with delimited keys. ``flatdict`` supports Python 3.5+.

Jump to :ref:`installation`, :ref:`example`, or :ref:`docs`.

*For example:*

.. code-block:: python

    value = flatdict.FlatDict({'foo': {'bar': 'baz', 'qux': 'corge'}})

*can be accessed as:*

.. code-block:: python

    value == {'foo:bar': 'baz', 'foo:qux': 'corge'}

*values can be accessed as:*

.. code-block:: python

    print(foo['foo:bar'])

    # or

    print(foo['foo']['bar'])

Additionally, lists and tuples are also converted into dicts using enumerate(),
using the :py:class:`~flatdict.FlatterDict` class.

*For example:*

.. code-block:: python

    value = flatdict.FlatterDict({'list': ['a', 'b', 'c']})

*will be flattened as follows:*

.. code-block:: python

    value == {'list:0': 'a', 'list:1': 'b', 'list:2': 'c'}

.. _installation:

Installation
------------

.. code-block:: bash

    $ pip install flatdict

Versioning
----------

This package attempts to use semantic versioning. API changes are indicated
by the major version, non-breaking improvements by the minor, and bug fixes
in the revision.

It is recommended that you pin your targets to greater or equal to the current
version and less than the next major version.

.. _example:

Example Use
-----------

:py:class:`flatdict.FlatDict`

.. code-block:: python

    import pprint

    import flatdict

    flat = flatdict.FlatDict(
        {'foo': {'bar': {'baz': 0,
                                'qux': 1,
                                'corge': 2},
                        'grault': {'baz': 3,
                                    'qux': 4,
                                    'corge': 5}},
                'garply': {'foo': 0, 'bar': 1, 'baz': 2, 'qux': {'corge': 3}}})

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

:py:class:`flatdict.FlatterDict`

.. code-block:: python

    import flatdict

    value = flatdict.FlatterDict({'list': ['a', 'b', 'c']})
    for key, value in value.items():
        print(key, value)

.. _docs:

API Documentation
-----------------

.. automodule:: flatdict
    :members:
    :undoc-members:
    :inherited-members:

.. |Version| image:: https://img.shields.io/pypi/v/flatdict.svg?
   :target: https://pypi.python.org/pypi/flatdict

.. |Status| image:: https://github.com/gmr/flatdict/workflows/Testing/badge.svg
   :target: https://github.com/gmr/flatdict/actions
   :alt: Build Status

.. |Coverage| image:: https://img.shields.io/codecov/c/github/gmr/flatdict.svg?
   :target: https://codecov.io/github/gmr/flatdict?branch=master

.. |License| image:: https://img.shields.io/pypi/l/flatdict.svg?
   :target: https://flatdict.readthedocs.org
