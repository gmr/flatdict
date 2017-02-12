"""
Unittests for flatdict.FlatDict

"""
try:
    import unittest2 as unittest
except ImportError:
    import unittest

import flatdict


class FlatDictTests(unittest.TestCase):

    KEYS = ['foo:bar:baz',
            'foo:bar:qux',
            'foo:bar:corge',
            'foo:grault:baz',
            'foo:grault:qux',
            'foo:grault:corge',
            'foo:list:0',
            'foo:list:1',
            'foo:list:2',
            'foo:tuple:0',
            'foo:tuple:1',
            'foo:tuple:2',
            'garply:foo',
            'garply:bar',
            'garply:baz',
            'garply:qux:corge']

    VALUES = {'foo': {'bar': {'baz': 0,
                              'qux': 1,
                              'corge': 2},
                      'grault': {'baz': 3,
                                 'qux': 4,
                                 'corge': 5},
                      'list': ['F', 'O', 'O',],
                      'tuple': ('F', 0, 0,)},
              'garply': {'foo': 0, 'bar': 1, 'baz': 2, 'qux': {'corge': 3}}}

    def setUp(self):
        self.object = flatdict.FlatDict(self.VALUES)
        self.keys = sorted(self.KEYS)

    def tearDown(self):
        del self.object

    def test_contains_true(self):
        self.assertTrue(self.keys[0] in self.object)

    def test_contains_false(self):
        self.assertFalse('foo:badkey' in self.object)

    def test_contains_nested_true(self):
        self.assertTrue('bar' in self.object['foo'])

    def test_contains_nested_false(self):
        self.assertTrue('bar' in self.object['garply'])

    def test_raises_key_error(self):
        self.assertRaises(KeyError, self.object.__getitem__, 'grault')

    def test_delitem(self):
        key = self.keys[0]
        if key not in self.object:
            assert False, 'Missing key in test object'
        del self.object[key]
        self.assertTrue(key not in self.object)

    def test_as_dict(self):
        flat_dict_value = flatdict.FlatDict(self.VALUES)
        self.assertDictEqual(flat_dict_value.as_dict(), self.VALUES)

    def test_clear(self):
        self.object.clear()
        self.assertDictEqual(self.object, dict())

    def test_copy(self):
        expectation = {'foo:bar:baz': 0,
                       'foo:bar:qux': 1,
                       'foo:bar:corge': 2,
                       'foo:grault:baz': 3,
                       'foo:grault:qux': 4,
                       'foo:grault:corge': 5,
                       'foo:list:0': 'F',
                       'foo:list:1': 'O',
                       'foo:list:2': 'O',
                       'foo:tuple:0': 'F',
                       'foo:tuple:1': 0,
                       'foo:tuple:2': 0,
                       'garply:foo': 0,
                       'garply:bar': 1,
                       'garply:baz': 2,
                       'garply:qux:corge': 3}
        self.assertDictEqual(self.object.copy(), expectation)

    def test_getitem_flat(self):
        key = 'foo:grault:qux'
        expectation = 4
        self.assertEqual(self.object[key], expectation)

    def test_getitem_flat_keyerror(self):
        getfunc = lambda k: self.object[k]
        self.assertRaises(KeyError, getfunc, 'foo:badkey')
        self.assertRaises(KeyError, getfunc, 'foo:grault:badkey')

    def test_get_flat(self):
        key = 'foo:grault:qux'
        expectation = 4
        self.assertEqual(self.object.get(key), expectation)

    def test_getitem_flat_sub(self):
        key = 'foo:grault'
        expectation = {'baz': 3, 'qux': 4, 'corge': 5}
        result = self.object[key]
        for key in expectation:
            self.assertEqual(result[key], expectation[key])

    def test_get_nested_sub(self):
        expectation = {'qux': 4, 'baz': 3, 'corge': 5}
        result = self.object['foo'].get('grault')
        for key in expectation:
            self.assertEqual(result[key], expectation[key])

    def test_get_none(self):
        self.assertEqual(self.object.get('Hi'), None)

    def test_has_key_true(self):
        self.assertTrue(self.object.has_key('foo:bar:baz'))

    def test_has_key_false(self):
        self.assertFalse(self.object.has_key('foo:bar:grault'))

    def test_items(self):
        expectation = [('foo:bar:baz', 0),
                       ('foo:bar:qux', 1),
                       ('foo:bar:corge', 2),
                       ('foo:grault:baz', 3),
                       ('foo:grault:qux', 4),
                       ('foo:grault:corge', 5),
                       ('foo:list:0', 'F'),
                       ('foo:list:1', 'O'),
                       ('foo:list:2', 'O'),
                       ('foo:tuple:0', 'F'),
                       ('foo:tuple:1', 0),
                       ('foo:tuple:2', 0),
                       ('garply:foo', 0),
                       ('garply:bar', 1),
                       ('garply:baz', 2),
                       ('garply:qux:corge', 3)]
        self.assertEqual(sorted(self.object.items()), sorted(expectation))

    def test_iteritems(self):
        expectation = [('foo:bar:baz', 0),
                       ('foo:bar:qux', 1),
                       ('foo:bar:corge', 2),
                       ('foo:grault:baz', 3),
                       ('foo:grault:qux', 4),
                       ('foo:grault:corge', 5),
                       ('foo:list:0', 'F'),
                       ('foo:list:1', 'O'),
                       ('foo:list:2', 'O'),
                       ('foo:tuple:0', 'F'),
                       ('foo:tuple:1', 0),
                       ('foo:tuple:2', 0),
                       ('garply:foo', 0),
                       ('garply:bar', 1),
                       ('garply:baz', 2),
                       ('garply:qux:corge', 3)]
        for value in self.object.iteritems():
            self.assertTrue(value in expectation)

    def test_iter(self):
        keys = [key for key in self.object]
        self.assertEqual(sorted(keys), self.keys)

    def test_iterkeys(self):
        for key in self.object.iterkeys():
            self.assertTrue(key in self.keys)

    def test_itervalues(self):
        values = (0, 1, 2, 3, 4, 5, 'F', 'O')
        for value in self.object.itervalues():
            self.assertTrue(value in values,
                            '%s is not in %r' % (value, values))

    def test_keys(self):
        self.assertListEqual(sorted(self.object.keys()), self.keys)

    def test_repr(self):
        result = repr(self.object)
        for key in self.keys:
            self.assertTrue(key in result)

    def test_str(self):
        result = str(self.object)
        for key in self.keys:
            self.assertTrue(key in result)

    def test_setdefault_flat_missing(self):
        key = 'abc:def:ghi'
        value = 10
        self.object.setdefault(key, value)
        self.assertEqual(self.object[key], value)

    def test_setitem_raises_type_error(self):
        self.object['test'] = 123
        self.assertRaises(TypeError, self.object.setdefault, 'test:foo', 4)

    def test_pop_flat(self):
        key = 'foo:bar:qux'
        value = 1
        response = self.object.pop(key)
        self.assertEqual(response, value)
        self.assertTrue(key not in self.object)

    def test_pop_none(self):
        self.assertTrue(self.object.pop('TEST', None) is None)

    def test_pop_top(self):
        key = 'foo'
        expectation = flatdict.FlatDict({'bar:baz': 0,
                                         'bar:qux': 1,
                                         'bar:corge': 2,
                                         'grault:baz': 3,
                                         'grault:qux': 4,
                                         'grault:corge': 5,
                                         'foo:list:0': 'F',
                                         'foo:list:1': 'O',
                                         'foo:list:2': 'O',
                                         'foo:tuple:0': 'F',
                                         'foo:tuple:1': 0,
                                         'foo:tuple:2': 0})
        response = self.object.pop(key)
        self.assertDictEqual(response, expectation)
        self.assertTrue(key not in self.object)

    def test_update_flat(self):
        expectation = flatdict.FlatDict({'foo:bar:baz': 4,
                                         'foo:bar:qux': 5,
                                         'foo:bar:corge': 6,
                                         'foo:grault:baz': 3,
                                         'foo:grault:qux': 4,
                                         'foo:grault:corge': 5,
                                         'garply:foo': 0,
                                         'garply:bar': 1,
                                         'garply:baz': 2,
                                         'garply:qux:corge': 3,
                                         'foo:list:0': 'F',
                                         'foo:list:1': 'O',
                                         'foo:list:2': 'O',
                                         'foo:tuple:0': 'F',
                                         'foo:tuple:1': 0,
                                         'foo:tuple:2': 0})
        self.object.update({'foo:bar:baz': 4,
                            'foo:bar:qux': 5,
                            'foo:bar:corge': 6})
        self.assertDictEqual(self.object, expectation)

    def test_values(self):
        expectation = [0, 1, 2, 3, 4, 5]
        values = self.object.values()
        for value in expectation:
            self.assertTrue(value in values,
                            '%s is not in %r' % (value, values))


class FlatDictDelimiterTests(FlatDictTests):

    def setUp(self):
        self.object = flatdict.FlatDict(self.VALUES, '-')
        self.keys = sorted([k.replace(':', '-') for k in self.KEYS])

    def test_contains_false(self):
        self.assertFalse('foo-badkey' in self.object)

    def test_contains_nested_true(self):
        self.assertTrue('bar' in self.object['foo'])

    def test_contains_nested_false(self):
        self.assertTrue('bar' in self.object['garply'])

    def test_raises_key_error(self):
        self.assertRaises(KeyError, self.object.__getitem__, 'grault')

    def test_delitem(self):
        key = self.keys[0]
        if key not in self.object:
            assert False, 'Missing key in test object'
        del self.object[key]
        self.assertTrue(key not in self.object)

    def test_copy(self):
        expectation = {'foo-bar-baz': 0,
                       'foo-bar-qux': 1,
                       'foo-bar-corge': 2,
                       'foo-grault-baz': 3,
                       'foo-grault-qux': 4,
                       'foo-grault-corge': 5,
                       'garply-foo': 0,
                       'garply-bar': 1,
                       'garply-baz': 2,
                       'garply-qux-corge': 3,
                       'foo-list-0': 'F',
                       'foo-list-1': 'O',
                       'foo-list-2': 'O',
                       'foo-tuple-0': 'F',
                       'foo-tuple-1': 0,
                       'foo-tuple-2': 0}
        self.assertDictEqual(self.object.copy(), expectation)

    def test_getitem_flat(self):
        key = 'foo-grault-qux'
        expectation = 4
        self.assertEqual(self.object[key], expectation)

    def test_getitem_flat_keyerror(self):
        getfunc = lambda k: self.object[k]
        self.assertRaises(KeyError, getfunc, 'foo-badkey')
        self.assertRaises(KeyError, getfunc, 'foo-grault-badkey')

    def test_get_flat(self):
        key = 'foo-grault-qux'
        expectation = 4
        self.assertEqual(self.object.get(key), expectation)

    def test_getitem_flat_sub(self):
        key = 'foo-grault'
        expectation = {'baz': 3, 'qux': 4, 'corge': 5}
        result = self.object[key]
        for key in expectation:
            self.assertEqual(result[key], expectation[key])

    def test_get_nested_sub(self):
        expectation = {'qux': 4, 'baz': 3, 'corge': 5}
        result = self.object['foo'].get('grault')
        for key in expectation:
            self.assertEqual(result[key], expectation[key])

    def test_has_key_true(self):
        self.assertTrue(self.object.has_key('foo-bar-baz'))

    def test_has_key_false(self):
        self.assertFalse(self.object.has_key('foo-bar-grault'))

    def test_items(self):
        expectation = [('foo-bar-baz', 0),
                       ('foo-bar-qux', 1),
                       ('foo-bar-corge', 2),
                       ('foo-grault-baz', 3),
                       ('foo-grault-qux', 4),
                       ('foo-grault-corge', 5),
                       ('garply-foo', 0),
                       ('garply-bar', 1),
                       ('garply-baz', 2),
                       ('garply-qux-corge', 3),
                       ('foo-list-0', 'F'),
                       ('foo-list-1', 'O'),
                       ('foo-list-2', 'O'),
                       ('foo-tuple-0', 'F'),
                       ('foo-tuple-1', 0),
                       ('foo-tuple-2', 0)]
        self.assertEqual(sorted(self.object.items()), sorted(expectation))

    def test_iteritems(self):
        expectation = [('foo-bar-baz', 0),
                       ('foo-bar-qux', 1),
                       ('foo-bar-corge', 2),
                       ('foo-grault-baz', 3),
                       ('foo-grault-qux', 4),
                       ('foo-grault-corge', 5),
                       ('garply-foo', 0),
                       ('garply-bar', 1),
                       ('garply-baz', 2),
                       ('garply-qux-corge', 3),
                       ('foo-list-0', 'F'),
                       ('foo-list-1', 'O'),
                       ('foo-list-2', 'O'),
                       ('foo-tuple-0', 'F'),
                       ('foo-tuple-1', 0),
                       ('foo-tuple-2', 0)]
        for value in self.object.iteritems():
            self.assertTrue(value in expectation)

    def test_setdefault_flat_missing(self):
        key = 'abc-def-ghi'
        value = 10
        self.object.setdefault(key, value)
        self.assertEqual(self.object[key], value)

    def test_setitem_raises_type_error(self):
        self.object['test'] = 123
        self.assertRaises(TypeError, self.object.setdefault, 'test-foo', 4)

    def test_pop_flat(self):
        key = 'foo-bar-qux'
        value = 1
        response = self.object.pop(key)
        self.assertEqual(response, value)
        self.assertTrue(key not in self.object)

    def test_pop_top(self):
        key = 'foo'
        expectation = flatdict.FlatDict({'bar-baz': 0,
                                         'bar-qux': 1,
                                         'bar-corge': 2,
                                         'grault-baz': 3,
                                         'grault-qux': 4,
                                         'grault-corge': 5,
                                         'foo:list:0': 'F',
                                         'foo:list:1': 'O',
                                         'foo:list:2': 'O',
                                         'foo:tuple:0': 'F',
                                         'foo:tuple:1': 0,
                                         'foo:tuple:2': 0})
        response = self.object.pop(key)
        self.assertDictEqual(response, expectation)
        self.assertTrue(key not in self.object)

    def test_update_flat(self):
        expectation = flatdict.FlatDict({'foo-bar-baz': 4,
                                         'foo-bar-qux': 5,
                                         'foo-bar-corge': 6,
                                         'foo-grault-baz': 3,
                                         'foo-grault-qux': 4,
                                         'foo-grault-corge': 5,
                                         'garply-foo': 0,
                                         'garply-bar': 1,
                                         'garply-baz': 2,
                                         'garply-qux-corge': 3,
                                         'foo:list:0': 'F',
                                         'foo:list:1': 'O',
                                         'foo:list:2': 'O',
                                         'foo:tuple:0': 'F',
                                         'foo:tuple:1': 0,
                                         'foo:tuple:2': 0})
        self.object.update({'foo-bar-baz': 4,
                            'foo-bar-qux': 5,
                            'foo-bar-corge': 6})
        self.assertDictEqual(self.object, expectation)


class FlatDictSetDelimiterTests(FlatDictDelimiterTests):

    def setUp(self):
        self.object = flatdict.FlatDict(self.VALUES, '^')
        self.object.set_delimiter('-')
        self.keys = sorted([k.replace(':', '-') for k in self.KEYS])


class FlatDictListAwarenessTests(unittest.TestCase):

    DOCUMENT = {
        "admiring": "allen",
        "wonderful": "archimedes",
        "quirky": [
            {
                "nifty": "khorana",
                "nostalgic": "lichterman",
                "gallant": [
                    "bhaskara",
                    "darwin",
                    "meninsky"
                ]
            },
            {
                "nifty": "jennings",
                "nostalgic": "hermann",
            },
            "condescending liskov"
        ],
        "flamboyant": "swartz"
    }

    KEYS = [
        'admiring',
        'wonderful',
        'quirky:0:nifty',
        'quirky:0:nostalgic',
        'quirky:0:gallant:0',
        'quirky:0:gallant:1',
        'quirky:0:gallant:2',
        'quirky:1:nifty',
        'quirky:1:nostalgic',
        'quirky:2',
        'flamboyant'
    ]

    def setUp(self):
        self.dict = flatdict.FlatDict(self.DOCUMENT, as_dict_list_awareness=True)
        self.keys = sorted(self.KEYS)

    def test_flatten_keys_are_created_as_expected(self):
        self.assertEqual(self.keys, sorted([key for key in self.dict]))

    def test_as_dict_returns_object_with_properly_constructed_lists(self):
        self.assertEqual(self.DOCUMENT, self.dict.as_dict())
