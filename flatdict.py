"""
FlatDict Implementation

"""
__author__ = 'Gavin M. Roy <gmr@meetme.com>'
__version__ = '1.1.0'

import json


class FlatDict(dict):
    """FlatDict is a dict object that allows for single level, delimited
    key/value pair mapping of nested dictionaries.

    For example:

        foo = {'foo': {'bar': 'baz', 'qux': 'corge'}}

    is represented as:

        {'foo:bar': 'baz',
         'foo'qux': 'corge'}

    And can still be accessed as:

        foo['foo']['bar']

    and

        foo['foo:bar']

    """
    DELIMITER = ':'

    def __init__(self, value=None):
        super(FlatDict, self).__init__()
        self._values = dict()
        if isinstance(value, dict):
            for key in value:
                self.__setitem__(key, value[key])

    def __contains__(self, key):
        if self.DELIMITER not in key:
            return key in self._values
        parent, child = key.split(self.DELIMITER, 1)
        return parent in self._values and child in self._values[parent]

    def __delitem__(self, key):
        if self.DELIMITER not in key:
            del self._values[key]
        else:
            parent, child = key.split(self.DELIMITER, 1)
            if (parent in self._values and
                child in self._values[parent]):
                del self._values[parent][child]
                if not self._values[parent]:
                    del self._values[parent]

    def __getitem__(self, key):
        if self.DELIMITER not in key:
            return self._values[key]
        parent, child = key.split(self.DELIMITER, 1)
        if parent in self._values:
            if child in self._values[parent]:
                child_value = self._values[parent][child]
                if isinstance(child_value, FlatDict):
                    value = dict()
                    for child_key in child_value.keys():
                        value[self._key(parent,child_key)] = child_value
                    return child_value
                return child_value

    def __iter__(self):
        for key in self.keys():
            yield key

    def __len__(self):
        return len(self.keys())

    def __repr__(self):
        values = dict()
        for key in self.keys():
            values[key] = self.__getitem__(key)
        return values.__repr__()

    def __setitem__(self, key, value):
        if isinstance(value, dict) and not isinstance(value, FlatDict):
            value = FlatDict(value)
        if self.DELIMITER in  key:
            parent_key, child_key = key.split(self.DELIMITER, 1)
            if parent_key not in self._values:
                self._values[parent_key] = FlatDict()
            parent = self._values.get(parent_key)
            if not isinstance(parent, FlatDict):
                raise TypeError('Top level node is not a FlatDict: %s',
                                parent_key, type(self._values[parent_key]))
            self._values[parent_key][child_key] = value
        else:
            self._values[key] = value

    def __str__(self):
        values = dict()
        for key in self.keys():
            values[key] = self.__getitem__(key)
        return values.__str__()

    def _key(self, parent, child):
        return self.DELIMITER.join([parent, child])

    def as_dict(self):
        dict_out = dict()
        for key in self._values.keys():
            if isinstance(self._values[key], FlatDict):
                dict_out[key] = self._values[key].as_dict()
            else:
                dict_out[key] = self._values[key]
        return dict_out

    def clear(self):
        self._values.clear()

    def copy(self):
        values = dict()
        for key in self.keys():
            values[key] = self.__getitem__(key)
        return values

    def get(self, key, d=None):
        if key not in self.keys():
            return self._values.get(key, d)
        return self.__getitem__(key)

    def has_key(self, key):
        return key in self.keys()

    def items(self):
        items = list()
        for key in self.keys():
            items.append((key, self.__getitem__(key)))
        return items

    def iteritems(self):
        for item in self.items():
            yield item

    def iterkeys(self):
        for key in self.keys():
            yield key

    def itervalues(self):
        for key in self.keys():
            yield self.__getitem__(key)

    def keys(self):
        keys = list()
        for key in self._values.keys():
            if isinstance(self._values[key], FlatDict):
                child_keys = self._values[key].keys()
                for child in child_keys:
                    keys.append(self._key(key, child))
            else:
                keys.append(key)
        return keys

    def pop(self, key, d=None):
        if key not in self.keys() and key not in self._values:
            return d
        if key in self._values:
            return self._values.pop(key, d)
        value = self.__getitem__(key)
        self.__delitem__(key)
        return value

    def setdefault(self, key, default):
        if key not in self:
            self[key] = default
        return self[key]

    def update(self, other=None, **kwargs):
        values = other or kwargs
        if values:
            for key in values:
                self.__setitem__(key, values[key])

    def values(self):
        values = list()
        for key in self.keys():
            values.append(self.__getitem__(key))
        return values

