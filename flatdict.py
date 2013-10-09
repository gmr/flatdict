"""FlatDict is a dict object that allows for single level, delimited
key/value pair mapping of nested dictionaries.

"""
__author__ = 'Gavin M. Roy <gavinmroy@gmail.com>'
__version__ = '1.1.1'


class FlatDict(dict):
    """:py:class:`~flatdict.FlatDict` is a dictionary object that allows for
    single level, delimited key/value pair mapping of nested dictionaries.
    The default delimiter value is ``:`` but can be changed in the constructor
    or by calling
    :py:class:`FlatDict.set_delimiter <flatdict.FlatDict.set_delimiter>`.

    """

    # The default delimiter value
    DELIMITER = ':'

    def __init__(self, value=None, delimiter=None):
        super(FlatDict, self).__init__()
        self._values = dict()
        self._delimiter = delimiter or self.DELIMITER
        if isinstance(value, dict):
            for key in value:
                self.__setitem__(key, value[key])

    def __contains__(self, key):
        if self._delimiter not in key:
            return key in self._values
        parent, child = key.split(self._delimiter, 1)
        return parent in self._values and child in self._values[parent]

    def __delitem__(self, key):
        if self._delimiter not in key:
            del self._values[key]
        else:
            parent, child = key.split(self._delimiter, 1)
            if (parent in self._values and
                child in self._values[parent]):
                del self._values[parent][child]
                if not self._values[parent]:
                    del self._values[parent]

    def __getitem__(self, key):
        if self._delimiter not in key:
            return self._values[key]
        parent, child = key.split(self._delimiter, 1)
        if parent in self._values and child in self._values[parent]:
            return self._values[parent][child]
        else:
            raise KeyError(key)

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
            value = FlatDict(value, self._delimiter)
        if self._delimiter in key:
            parent_key, child_key = key.split(self._delimiter, 1)
            if parent_key not in self._values:
                self._values[parent_key] = FlatDict(delimiter=self._delimiter)
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
        return self._delimiter.join([parent, child])

    def as_dict(self):
        """Return the flat dictionary as a dictionary.

        :rtype: dict

        """
        dict_out = dict()
        for key in self._values.keys():
            if isinstance(self._values[key], FlatDict):
                dict_out[key] = self._values[key].as_dict()
            else:
                dict_out[key] = self._values[key]
        return dict_out

    def clear(self):
        """Remove all items from the flat dictionary."""
        self._values.clear()

    def copy(self):
        """Return a shallow copy of the flat dictionary.

        :rtype: flatdict.FlatDict

        """
        values = dict()
        for key in self.keys():
            values[key] = self.__getitem__(key)
        return values

    def get(self, key, d=None):
        """Return the value for key if key is in the flat dictionary, else
        default. If default is not given, it defaults to ``None``, so that this
        method never raises a ``KeyError``.

        :param mixed key: The key to get
        :param mixed d: The default value
        :rtype: mixed

        """
        if key not in self.keys():
            return self._values.get(key, d)
        return self.__getitem__(key)

    def has_key(self, key):
        """Check to see if the flat dictionary has a specific key.

        :param mixed key: The key to check for
        :rtype: bool

        """
        return key in self.keys()

    def items(self):
        """Return a copy of the flat dictionary's list of ``(key, value)``
        pairs.

        .. note:: CPython implementation detail: Keys and values are listed in \
        an arbitrary order which is non-random, varies across Python \
        implementations, and depends on the flat dictionary's history of \
        insertions and deletions.

        :rtype: list

        """
        items = list()
        for key in self.keys():
            items.append((key, self.__getitem__(key)))
        return items

    def iteritems(self):
        """Return an iterator over the flat dictionary's (key, value) pairs.
        See the note for :py:class:`FlatDict.items() <flatdict.FlatDict.items>`.

        Using ``iteritems()`` while adding or deleting entries in the flat
        dictionary may raise a ``RuntimeError`` or fail to iterate over all
        entries.

        :rtype: Iterator
        :raises: RuntimeError

        """
        for item in self.items():
            yield item

    def iterkeys(self):
        """Return an iterator over the flat dictionary's keys. See the note for
        :py:class:`FlatDict.items() <flatdict.FlatDict.items>`.

        Using ``iterkeys()`` while adding or deleting entries in the flat
        dictionary may raise a ``RuntimeError`` or fail to iterate over all
        entries.

        :rtype: Iterator
        :raises: RuntimeError

        """

        for key in self.keys():
            yield key

    def itervalues(self):
        """Return an iterator over the flat dictionary's values. See the note
        for :py:class:`FlatDict.items() <flatdict.FlatDict.items>`.

        Using ``itervalues()`` while adding or deleting entries in the flat
        dictionary may raise a ``RuntimeError`` or fail to iterate over all
        entries.

        :rtype: Iterator
        :raises: RuntimeError

        """
        for key in self.keys():
            yield self.__getitem__(key)

    def keys(self):
        """Return a copy of the flat dictionary's list of keys. See the note for
        :py:class:`FlatDict.items() <flatdict.FlatDict.items>`.

        :rtype: list

        """
        keys = list()
        for key in self._values.keys():
            if isinstance(self._values[key], FlatDict):
                child_keys = self._values[key].keys()
                for child in child_keys:
                    keys.append(self._key(key, child))
            else:
                keys.append(key)
        return keys

    def pop(self, key, default=None):
        """If key is in the flat dictionary, remove it and return its value,
        else return default. If default is not given and key is not in the
        dictionary, a ``KeyError`` is raised.

        :param mixed key: The key name
        :param mixed default: The default value
        :rtype: mixed

        """
        if key not in self.keys() and key not in self._values:
            return default
        if key in self._values:
            return self._values.pop(key, default)
        value = self.__getitem__(key)
        self.__delitem__(key)
        return value

    def setdefault(self, key, default):
        """ If key is in the flat dictionary, return its value. If not,
        insert key with a value of default and return default.
        default defaults to ``None``.

        :param mixed key: The key name
        :param mixed default: The default value
        :rtype: mixed

        """
        print('setdefault: %s' % key)
        if key not in self:
            self.__setitem__(key, default)
        return self.__getitem__(key)

    def set_delimiter(self, delimiter):
        """Override the default or passed in delimiter with a new value.

        :param str delimiter: The delimiter to use

        """
        self._delimiter = delimiter
        for key in self._values.keys():
            if isinstance(self._values[key], FlatDict):
                self._values[key].set_delimiter(delimiter)

    def update(self, other=None, **kwargs):
        """Update the flat dictionary with the key/value pairs from other,
        overwriting existing keys.

        ``update()`` accepts either another flat dictionary object or an
        iterable of key/value pairs (as tuples or other iterables of length
        two). If keyword arguments are specified, the flat dictionary is then
        updated with those key/value pairs: ``d.update(red=1, blue=2)``.

        :rtype: None

        """
        values = other or kwargs
        if values:
            for key in values:
                self.__setitem__(key, values[key])

    def values(self):
        """Return a copy of the flat dictionary's list of values. See the note
        for :py:class:`FlatDict.items() <flatdict.FlatDict.items>`.

        :rtype: list

        """
        values = list()
        for key in self.keys():
            values.append(self.__getitem__(key))
        return values

