"""
Unittests for flatdict.FlatDict

"""
import pickle
import random
import unittest
import uuid

import flatdict


class FlatDictTests(unittest.TestCase):

    TEST_CLASS = flatdict.FlatDict

    FLAT_EXPECTATION = {
        'foo:bar:baz': 0,
        'foo:bar:qux': 1,
        'foo:bar:corge': 2,
        'foo:grault:baz': 3,
        'foo:grault:qux': 4,
        'foo:grault:corge': 5,
        'foo:list': ['F', 'O', 'O'],
        'foo:empty_list': [],
        'foo:set': {10, 20, 30},
        'foo:empty_set': set(),
        'foo:tuple': ('F', 0, 0),
        'foo:empty_tuple': (),
        'garply:foo': 0,
        'garply:bar': 1,
        'garply:baz': 2,
        'garply:qux:corge': 3,
        'fred': 4,
        'xyzzy': 'plugh',
        'thud': 5,
        'waldo:fred': 6,
        'waldo:wanda': 7
    }

    KEYS = [
        'foo:bar:baz', 'foo:bar:qux', 'foo:bar:corge', 'foo:grault:baz',
        'foo:grault:qux', 'foo:grault:corge', 'foo:list', 'foo:empty_list',
        'foo:set', 'foo:empty_set', 'foo:tuple', 'foo:empty_tuple',
        'garply:foo', 'garply:bar', 'garply:baz', 'garply:qux:corge', 'fred',
        'xyzzy', 'thud', 'waldo:fred', 'waldo:wanda'
    ]

    VALUES = {
        'foo': {
            'bar': {
                'baz': 0,
                'qux': 1,
                'corge': 2
            },
            'grault': {
                'baz': 3,
                'qux': 4,
                'corge': 5
            },
            'list': ['F', 'O', 'O'],
            'empty_list': [],
            'set': {10, 20, 30},
            'empty_set': set(),
            'tuple': ('F', 0, 0),
            'empty_tuple': ()

        },
        'garply': {
            'foo': 0,
            'bar': 1,
            'baz': 2,
            'qux': {
                'corge': 3
            }
        },
        'fred': 4,
        'xyzzy': 'plugh',
        'thud': 5,
        'waldo:fred': 6,
        'waldo:wanda': 7
    }

    AS_DICT = {
        'foo': {
            'bar': {
                'baz': 0,
                'qux': 1,
                'corge': 2
            },
            'grault': {
                'baz': 3,
                'qux': 4,
                'corge': 5
            },
            'list': ['F', 'O', 'O'],
            'empty_list': [],
            'set': {10, 20, 30},
            'empty_set': set(),
            'tuple': ('F', 0, 0),
            'empty_tuple': (),
        },
        'garply': {
            'foo': 0,
            'bar': 1,
            'baz': 2,
            'qux': {
                'corge': 3
            }
        },
        'fred': 4,
        'xyzzy': 'plugh',
        'thud': 5,
        'waldo': {
            'fred': 6,
            'wanda': 7
        }
    }

    def setUp(self):
        self.value = self.TEST_CLASS(self.VALUES, ':')

    def test_contains_true(self):
        self.assertTrue(all(k in self.value for k in self.KEYS))

    def test_contains_false(self):
        self.assertNotIn(str(uuid.uuid4()), self.value['foo'])

    def test_contains_nested_true(self):
        self.assertIn('bar', self.value['foo'])

    def test_contains_nested_false(self):
        self.assertIn('bar', self.value['garply'])

    def test_raises_key_error(self):
        self.assertRaises(KeyError, self.value.__getitem__, 'grault')

    def test_del_item(self):
        offset = random.randint(0, len(self.KEYS) - 1)
        del self.value[self.KEYS[offset]]
        self.assertNotIn(self.KEYS[offset], self.value)

    def test_del_top(self):
        del self.value['foo']
        for key in [k for k in self.KEYS if k.startswith('foo:')]:
            self.assertNotIn(key, self.value)

    def test_as_dict(self):
        self.assertDictEqual(self.value.as_dict(), self.AS_DICT)

    def test_cast_to_dict(self):
        self.assertDictEqual(dict(self.value), self.FLAT_EXPECTATION)

    def test_casting_items_to_dict(self):
        self.assertEqual(dict(self.value.items()), self.FLAT_EXPECTATION)

    def test_missing_key_on_del(self):
        with self.assertRaises(KeyError):
            del self.value[str(uuid.uuid4())]

    def test_missing_key_on_get(self):
        with self.assertRaises(KeyError):
            self.assertIsNotNone(self.value[str(uuid.uuid4())])

    def test_del_all_for_prefix(self):
        for key in [k for k in self.KEYS if k.startswith('garply')]:
            del self.value[key]
        self.assertNotIn('garply', self.value)

    def test_iter_keys(self):
        self.assertListEqual(sorted(self.KEYS),
                             sorted(k for k in iter(self.value)))

    def test_repr_value(self):
        value = self.TEST_CLASS({'foo': 'bar', 'baz': {'qux': 'corgie'}})
        self.assertIn(str(value), repr(value))
        self.assertEqual(
            repr(value)[0:len(self.TEST_CLASS.__name__) + 1],
            '<{}'.format(self.TEST_CLASS.__name__))

    def test_str_value(self):
        val = self.TEST_CLASS({'foo': 1, 'baz': {'qux': 'corgie'}})
        self.assertIn("'foo': 1", str(val))
        self.assertIn("'baz:qux': 'corgie'", str(val))

    def test_incorrect_assignment_raises(self):
        value = self.TEST_CLASS({'foo': ['bar'], 'qux': 1})
        with self.assertRaises(TypeError):
            value['foo:bar'] = 'baz'
        with self.assertRaises(TypeError):
            value['qux:baz'] = 'corgie'

    def test_clear(self):
        self.value.clear()
        self.assertDictEqual(self.value.as_dict(), {})

    def test_get(self):
        self.assertEqual(self.value.get('foo:bar:baz'), 0)

    def test_get_none_for_missing_key(self):
        self.assertIsNone(self.value.get(str(uuid.uuid4())))

    def test_copy(self):
        copied = self.value.copy()
        self.assertNotEqual(id(self.value), id(copied))
        self.assertDictEqual(self.value.as_dict(), copied.as_dict())

    def test_eq(self):
        self.assertEqual(self.value, self.value.copy())

    def test_eq_dict(self):
        self.assertEqual(self.value, self.value.as_dict())

    def test_not_eq(self):
        value = self.TEST_CLASS({'foo': ['bar']})
        self.assertFalse(self.value == value)

    def test_ne(self):
        value = self.TEST_CLASS({'foo': ['bar']})
        self.assertTrue(self.value != value)

    def test_eq_value_error(self):
        with self.assertRaises(TypeError):
            self.assertTrue(self.value == 123)

    def test_iter_items(self):
        items = [(k, v) for k, v in self.value.iteritems()]
        self.assertListEqual(self.value.items(), items)

    def test_iterkeys(self):
        keys = sorted(self.value.iterkeys())
        self.assertListEqual(keys, sorted(self.KEYS))

    def test_itervalues(self):
        values = list(self.value.itervalues())
        self.assertListEqual(values, self.value.values())

    def test_pop(self):
        self.assertEqual(1, self.value.pop('foo:bar:qux'))
        self.assertNotIn('foo:bar:qux', self.value)

    def test_pop_top(self):
        expectation = self.value.__class__(self.VALUES['foo'])
        self.assertEqual(expectation, self.value.pop('foo'))
        self.assertNotIn('foo', self.value)

    def test_pop_default(self):
        default = str(uuid.uuid4())
        self.assertEqual(self.value.pop(str(uuid.uuid4()), default), default)

    def test_pop_no_default(self):
        with self.assertRaises(KeyError):
            self.value.pop(str(uuid.uuid4()))

    def test_set_default(self):
        value = self.TEST_CLASS()
        value.setdefault('foo:bar:qux', 9999)
        self.assertEqual(value['foo:bar:qux'], 9999)

    def test_set_default_already_set(self):
        self.value.setdefault('foo:bar:qux', 9999)
        self.assertEqual(self.value['foo:bar:qux'], 1)

    def test_set_default_already_set_false_or_none(self):
        value = self.TEST_CLASS({'foo': False})
        value.setdefault('foo', None)
        self.assertEqual(value['foo'], False)

    def test_set_delimiter(self):
        self.value.set_delimiter('-')
        self.assertListEqual(
            sorted(k.replace(':', '-') for k in self.KEYS),
            sorted(self.value.keys()))
        self.assertListEqual(
            sorted(str(self.value[k.replace(':', '-')]) for k in self.KEYS),
            sorted(str(v) for v in self.value.values()))

    def test_update(self):
        expectation = self.TEST_CLASS(self.value.as_dict())
        expectation['foo:bar:baz'] = 4
        expectation['foo:bar:qux'] = 5
        expectation['foo:bar:corgie'] = 6
        expectation['foo:bar:waldo'] = 7
        self.value.update({
            'foo:bar:baz': 4,
            'foo:bar:qux': 5,
            'foo:bar:corgie': 6,
            'foo:bar:waldo': 7
        })
        self.assertEqual(self.value, expectation)

    def test_set_delimiter_collision(self):
        value = self.TEST_CLASS({'foo_bar': {'qux': 1}})
        with self.assertRaises(ValueError):
            value.set_delimiter('_')

    def test_pickling(self):
        pickled = pickle.dumps(self.value)
        self.assertEqual(pickle.loads(pickled), self.value)

    def test_empty_dict_as_value(self):
        expectation = {'foo': {'bar': {}}}
        flat = self.TEST_CLASS(expectation)
        value = flat.as_dict()
        self.assertDictEqual(value, expectation)


class FlatterDictTests(FlatDictTests):

    TEST_CLASS = flatdict.FlatterDict

    FLAT_EXPECTATION = {
        'foo:bar:baz': 0,
        'foo:bar:qux': 1,
        'foo:bar:corge': 2,
        'foo:bar:list:0': -1,
        'foo:bar:list:1': -2,
        'foo:bar:list:2': -3,
        'foo:grault:baz': 3,
        'foo:grault:qux': 4,
        'foo:grault:corge': 5,
        'foo:list:0': 'F',
        'foo:list:1': 'O',
        'foo:list:2': 'O',
        'foo:list:3': '',
        'foo:list:4': 'B',
        'foo:list:5': 'A',
        'foo:list:6': 'R',
        'foo:list:7': '',
        'foo:list:8': 'L',
        'foo:list:9': 'I',
        'foo:list:10': 'S',
        'foo:list:11': 'T',
        'foo:set:0': 10,
        'foo:set:1': 20,
        'foo:set:2': 30,
        'foo:tuple:0': 'F',
        'foo:tuple:1': 0,
        'foo:tuple:2': 0,
        'foo:abc:def': True,
        'garply:foo': 0,
        'garply:bar': 1,
        'garply:baz': 2,
        'garply:qux:corge': 3,
        'fred': 4,
        'xyzzy': 'plugh',
        'thud': 5,
        'waldo:fred': 6,
        'waldo:wanda': 7,
        'neighbors:0:left': 'john',
        'neighbors:0:right': 'michelle',
        'neighbors:1:left': 'steven',
        'neighbors:1:right': 'wynona',
        'double_nest:0:0': 1,
        'double_nest:0:1': 2,
        'double_nest:1:0': 3,
        'double_nest:1:1': 4,
        'double_nest:2:0': 5,
        'double_nest:2:1': 6,
    }

    KEYS = [
        'foo:bar:baz',
        'foo:bar:qux',
        'foo:bar:corge',
        'foo:bar:list:0',
        'foo:bar:list:1',
        'foo:bar:list:2',
        'foo:grault:baz',
        'foo:grault:qux',
        'foo:grault:corge',
        'foo:list:0',
        'foo:list:1',
        'foo:list:2',
        'foo:list:3',
        'foo:list:4',
        'foo:list:5',
        'foo:list:6',
        'foo:list:7',
        'foo:list:8',
        'foo:list:9',
        'foo:list:10',
        'foo:list:11',
        'foo:set:0',
        'foo:set:1',
        'foo:set:2',
        'foo:tuple:0',
        'foo:tuple:1',
        'foo:tuple:2',
        'foo:abc:def',
        'garply:foo',
        'garply:bar',
        'garply:baz',
        'garply:qux:corge',
        'fred',
        'xyzzy',
        'thud',
        'waldo:fred',
        'waldo:wanda',
        'neighbors:0:left',
        'neighbors:0:right',
        'neighbors:1:left',
        'neighbors:1:right',
        'double_nest:0:0',
        'double_nest:0:1',
        'double_nest:1:0',
        'double_nest:1:1',
        'double_nest:2:0',
        'double_nest:2:1',
    ]

    VALUES = {
        'foo': {
            'bar': {
                'baz': 0,
                'qux': 1,
                'corge': 2,
                'list': [-1, -2, -3]
            },
            'grault': {
                'baz': 3,
                'qux': 4,
                'corge': 5
            },
            'list': ['F', 'O', 'O', '', 'B', 'A', 'R', '', 'L', 'I', 'S', 'T'],
            'set': {10, 20, 30},
            'tuple': ('F', 0, 0),
            'abc': {
                'def': True
            }
        },
        'garply': {
            'foo': 0,
            'bar': 1,
            'baz': 2,
            'qux': {
                'corge': 3
            }
        },
        'fred': 4,
        'xyzzy': 'plugh',
        'thud': 5,
        'waldo:fred': 6,
        'waldo:wanda': 7,
        'neighbors': [{
            'left': 'john',
            'right': 'michelle'
        }, {
            'left': 'steven',
            'right': 'wynona'
        }],
        'double_nest': [
            [1, 2],
            (3, 4),
            {5, 6},
        ]
    }

    AS_DICT = {
        'foo': {
            'bar': {
                'baz': 0,
                'qux': 1,
                'corge': 2,
                'list': [-1, -2, -3]
            },
            'grault': {
                'baz': 3,
                'qux': 4,
                'corge': 5
            },
            'list': ['F', 'O', 'O', '', 'B', 'A', 'R', '', 'L', 'I', 'S', 'T'],
            'set': {10, 20, 30},
            'tuple': ('F', 0, 0),
            'abc': {
                'def': True
            }
        },
        'garply': {
            'foo': 0,
            'bar': 1,
            'baz': 2,
            'qux': {
                'corge': 3
            }
        },
        'fred':
        4,
        'xyzzy':
        'plugh',
        'thud':
        5,
        'waldo': {
            'fred': 6,
            'wanda': 7
        },
        'neighbors': [{
            'left': 'john',
            'right': 'michelle'
        }, {
            'left': 'steven',
            'right': 'wynona'
        }],
        'double_nest': [
            [1, 2],
            (3, 4),
            {5, 6},
        ]
    }

    def test_set_item(self):
        vals = {'double_nest': [[1, 2], [3, 4]]}
        d = self.TEST_CLASS(vals)
        new_vals = {'double_nest': [[-1, 2], [3, 4]]}
        d['double_nest:0:0'] = -1
        self.assertEqual(d.as_dict(), new_vals)

    def test_update_nest(self):
        vals = {'double_nest': [[1, 2], [3, 4]]}
        d = self.TEST_CLASS(vals)
        new_vals = {'double_nest': [[-1, 2], [3, 4]]}
        d.update(new_vals)
        self.assertEqual(d.as_dict(), new_vals)

    def test_set_nest_dict(self):
        vals = {'dicts': [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]}
        d = self.TEST_CLASS(vals)
        vals['dicts'][0]['a'] = -1
        d['dicts:0:a'] = -1
        self.assertEqual(d.as_dict(), vals)

    def test_update_nest_dict(self):
        vals = {'dicts': [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}]}
        d = self.TEST_CLASS(vals)
        vals['dicts'][0]['a'] = -1
        d.update(vals)
        self.assertEqual(d.as_dict(), vals)
