"""
Unittests for flatdict.FlatDict

"""
import pickle
import random
import unittest
import uuid

import flatdict


class FlatDictTests(unittest.TestCase):

    FLAT_EXPECTATION = {
        'foo:bar:baz': 0,
        'foo:bar:qux': 1,
        'foo:bar:corge': 2,
        'foo:grault:baz': 3,
        'foo:grault:qux': 4,
        'foo:grault:corge': 5,
        'foo:list': ['F', 'O', 'O'],
        'foo:set': {10, 20, 30},
        'foo:tuple': ('F', 0, 0),
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

    KEYS = sorted([
        'foo:bar:baz', 'foo:bar:qux', 'foo:bar:corge', 'foo:grault:baz',
        'foo:grault:qux', 'foo:grault:corge', 'foo:list', 'foo:set',
        'foo:tuple', 'garply:foo', 'garply:bar', 'garply:baz',
        'garply:qux:corge', 'fred', 'thud', 'xyzzy', 'waldo:fred',
        'waldo:wanda'
    ])

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
            'set': {10, 20, 30},
            'tuple': ('F', 0, 0)
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
            'set': {10, 20, 30},
            'tuple': ('F', 0, 0)
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
        self.value = flatdict.FlatDict(self.VALUES, ':')

    def test_contains_true(self):
        self.assertTrue(all([k in self.value for k in self.KEYS]))

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
        value = dict(self.value)
        self.assertDictEqual(value, self.FLAT_EXPECTATION)

    def test_casting_items_to_dict(self):
        self.assertEqual(dict(self.value.items()), self.FLAT_EXPECTATION)

    def test_missing_key_on_del(self):
        with self.assertRaises(KeyError):
            del self.value[str(uuid.uuid4())]

    def test_missing_key_on_get(self):
        with self.assertRaises(KeyError):
            x = self.value[str(uuid.uuid4())]

    def test_del_all_for_prefix(self):
        for key in [k for k in self.KEYS if k.startswith('garply')]:
            del self.value[key]
        self.assertNotIn('garply', self.value)

    def test_iter_keys(self):
        self.assertListEqual(
            sorted(self.KEYS), sorted([k for k in iter(self.value)]))

    def test_repr_value(self):
        val = flatdict.FlatDict({'foo': 'bar', 'baz': {'qux': 'corgie'}})
        self.assertEqual("\"{'baz:qux': 'corgie', 'foo': 'bar'}\"", repr(val))

    def test_str_value(self):
        val = flatdict.FlatDict({'foo': 'bar', 'baz': {'qux': 'corgie'}})
        self.assertEqual("{'baz:qux': 'corgie', 'foo': 'bar'}", str(val))

    def test_incorrect_assignment_raises(self):
        value = flatdict.FlatDict({'foo': ['bar']})
        with self.assertRaises(TypeError):
            value['foo:bar'] = 'baz'

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
        self.assertEqual(self.value,  self.value.copy())

    def test_eq_dict(self):
        self.assertEqual(self.value,  self.value.as_dict())

    def test_not_eq(self):
        value = flatdict.FlatDict({'foo': ['bar']})
        self.assertFalse(self.value == value)

    def test_ne(self):
        value = flatdict.FlatDict({'foo': ['bar']})
        self.assertTrue(self.value != value)

    def test_eq_value_error(self):
        with self.assertRaises(TypeError):
            a = self.value == 123

    def test_iter_items(self):
        items = [(k, v) for k, v in self.value.iteritems()]
        self.assertEqual(sorted(self.value.items()), items)

    def test_iterkeys(self):
        keys = [k for k in self.value.iterkeys()]
        self.assertEqual(keys, self.KEYS)

    def test_itervalues(self):
        values = [v for v in self.value.itervalues()]
        self.assertEqual(values, self.value.values())

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
        value = flatdict.FlatDict()
        value.setdefault('foo:bar:qux', 9999)
        self.assertEqual(value['foo:bar:qux'], 9999)

    def test_set_default_already_set(self):
        self.value.setdefault('foo:bar:qux', 9999)
        self.assertEqual(self.value['foo:bar:qux'], 1)

    def test_set_delimiter(self):
        self.value.set_delimiter('-')
        self.assertEqual([k.replace(':', '-') for k in self.KEYS],
                         self.value.keys())
        self.assertEqual([self.value[k.replace(':', '-')] for k in self.KEYS],
                         self.value.values())

    def test_update(self):
        expectation = flatdict.FlatDict(self.value.as_dict())
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
        value = flatdict.FlatDict({'foo_bar': {'qux': 1}})
        with self.assertRaises(ValueError):
            value.set_delimiter('_')

    def test_pickling(self):
        pickled = pickle.dumps(self.value)
        self.assertEqual(pickle.loads(pickled), self.value)
