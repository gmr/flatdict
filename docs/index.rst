.. FlatDict documentation master file, created by
   sphinx-quickstart on Tue Oct  8 23:46:29 2013.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

FlatDict
========
|PyPI version| |Downloads| |Build Status|

**FlatDict** is a Python module for interacting with nested dicts as a single
level dict with delimited keys. :py:class:`~flatdict.FlatDict` supports Python 2.6, 2.7, 3.2, and 3.3.

Jump to :ref:`installation`, :ref:`example`, :ref:`docs`, or :ref:`license`.

For example:

.. code-block:: python

    foo = {'foo': {'bar': 'baz', 'qux': 'corge'}}

is represented as:

.. code-block:: python

    {'foo:bar': 'baz',
     'foo:qux': 'corge'}

And can still be accessed as:

.. code-block:: python

    foo['foo']['bar']


and

.. code-block:: python

    foo['foo:bar']


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

.. _license:

License
=======
Copyright (c) 2013 Gavin M. Roy
All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

 * Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
 * Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.
 * Neither the name of the Flatdict nor the names of its
   contributors may be used to endorse or promote products derived from this
   software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


.. |PyPI version| image:: https://badge.fury.io/py/flatdict.png
   :target: http://badge.fury.io/py/flatdict
.. |Downloads| image:: https://pypip.in/d/flatdict/badge.png
   :target: https://crate.io/packages/flatdict
.. |Build Status| image:: https://travis-ci.org/gmr/flatdict.png?branch=master
   :target: https://travis-ci.org/gmr/flatdict