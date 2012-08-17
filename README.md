FlatDict
========

FlatDict is a dict object that allows for single level, delimited key/value pair
mapping of nested dictionaries. You can interact with FlatDict like a normal
dictionary and access child dicts as you normally would or with the composited
key.

For example:

    foo = {'foo': {'bar': 'baz', 'qux': 'corge'}}

is represented as:

    {'foo:bar': 'baz',
     'foo'qux': 'corge'}

And can still be accessed as:

    foo['foo']['bar']

and

    foo['foo:bar']

API
---
FlatDict has the same methods as dict in Python 2.6. In addition, it has a
FlatDict.as_dict method which will return a pure nested dictionary from a
FlatDict value.

Installation
------------
easy_install flatdict

Example Use
-----------

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
