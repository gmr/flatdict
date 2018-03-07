"""FlatDict is a dict object that allows for single level, delimited
key/value pair mapping of nested dictionaries.

"""
import collections

__version__ = '3.0.0'

NO_DEFAULT = object()


class FlatDict(collections.MutableMapping):
    """:class:`~flatdict.FlatDict` is a dictionary object that allows for
    single level, delimited key/value pair mapping of nested dictionaries.
    The default delimiter value is ``:`` but can be changed in the constructor
    or by calling :meth:`FlatDict.set_delimiter`.

    """
    _COERCE = dict

    def __init__(self, value=None, delimiter=':'):
        super(FlatDict, self).__init__()
        self._values = {}
        self._delimiter = delimiter
        self.update(value)

    def __contains__(self, key):
        """Check to see if the key exists, checking for both delimited and
        not delimited key values.

        :param mixed key: The key to check for

        """
        if self._has_delimiter(key):
            pk, ck = key.split(self._delimiter, 1)
            return pk in self._values and ck in self._values[pk]
        return key in self._values

    def __delitem__(self, key):
        """Delete the item for the specified key, automatically dealing with
        nested children.

        :param mixed key: The key to use
        :raises: KeyError

        """
        if key not in self:
            raise KeyError
        if self._has_delimiter(key):
            pk, ck = key.split(self._delimiter, 1)
            del self._values[pk][ck]
            if not self._values[pk]:
                del self._values[pk]
        else:
            del self._values[key]

    def __eq__(self, other):
        """Check for equality against the other value

        :param other: The value to compare
        :type other: FlatDict
        :rtype: bool
        :raises: TypeError

        """
        if isinstance(other, dict):
            return sorted(self.as_dict()) == sorted(other)
        elif not isinstance(other, self.__class__):
            raise TypeError
        return sorted(self.as_dict()) == sorted(other.as_dict())

    def __ne__(self, other):
        """Check for inequality against the other value

        :param other: The value to compare
        :type other: dict or FlatDict
        :rtype: bool

        """
        return not self.__eq__(other)

    def __getitem__(self, key):
        """Get an item for the specified key, automatically dealing with
        nested children.

        :param mixed key: The key to use
        :rtype: mixed
        :raises: KeyError

        """
        values = self._values
        for part in key.split(self._delimiter):
            values = values[part]
        return values

    def __iter__(self):
        """Iterate over the flat dictionary key and values

        :rtype: Iterator
        :raises: RuntimeError

        """
        return iter(self.keys())

    def __len__(self):
        """Return the number of items.

        :rtype: int

        """
        return len(self.keys())

    def __reduce__(self):
        """Return state information for pickling

        :rtype: tuple

        """
        return type(self), (self.as_dict(), self._delimiter)

    def __repr__(self):
        """Return the string representation of the instance.

        :rtype: str

        """
        return '"{}"'.format(str(self))

    def __setitem__(self, key, value):
        """Assign the value to the key, dynamically building nested
        FlatDict items where appropriate.

        :param mixed key: The key for the item
        :param mixed value: The value for the item
        :raises: TypeError

        """
        if isinstance(value, self._COERCE) and not isinstance(value, FlatDict):
            value = self.__class__(value, self._delimiter)
        if self._has_delimiter(key):
            pk, ck = key.split(self._delimiter, 1)
            if pk not in self._values:
                self._values[pk] = self.__class__({ck: value}, self._delimiter)
                return
            elif not isinstance(self._values[pk], FlatDict):
                raise TypeError(
                    'Assignment to invalid type for key {}'.format(pk))
            self._values[pk][ck] = value
        else:
            self._values[key] = value

    def __str__(self):
        """Return the string value of the instance.

        :rtype: str

        """
        return '{{{}}}'.format(', '.join([
            '{!r}: {!r}'.format(str(k), str(v))
            for k, v in sorted(self.items())
        ]))

    def as_dict(self):
        """Return the :class:`~flatdict.FlatDict` as a :class:`dict`

        :rtype: dict

        """
        out = dict({})
        for key in self.keys():
            if self._has_delimiter(key):
                pk, ck = key.split(self._delimiter, 1)
                if self._has_delimiter(ck):
                    ck = ck.split(self._delimiter, 1)[0]
                if isinstance(self._values[pk], FlatDict) and pk not in out:
                    out[pk] = dict()
                if isinstance(self._values[pk][ck], FlatDict):
                    out[pk][ck] = self._values[pk][ck].as_dict()
                else:
                    out[pk][ck] = self._values[pk][ck]
            else:
                out[key] = self._values[key]
        return out

    def clear(self):
        """Remove all items from the flat dictionary."""
        self._values.clear()

    def copy(self):
        """Return a shallow copy of the flat dictionary.

        :rtype: flatdict.FlatDict

        """
        return self.__class__(self.as_dict(), delimiter=self._delimiter)

    def get(self, key, d=None):
        """Return the value for key if key is in the flat dictionary, else
        default. If default is not given, it defaults to ``None``, so that this
        method never raises :exc:`KeyError`.

        :param mixed key: The key to get
        :param mixed d: The default value
        :rtype: mixed

        """
        try:
            return self.__getitem__(key)
        except KeyError:
            return d

    def items(self):
        """Return a copy of the flat dictionary's list of ``(key, value)``
        pairs.

        .. note:: CPython implementation detail: Keys and values are listed in
            an arbitrary order which is non-random, varies across Python
            implementations, and depends on the flat dictionary's history of
            insertions and deletions.

        :rtype: list

        """
        return [(k, self.__getitem__(k)) for k in self.keys()]

    def iteritems(self):
        """Return an iterator over the flat dictionary's (key, value) pairs.
        See the note for :meth:`flatdict.FlatDict.items`.

        Using ``iteritems()`` while adding or deleting entries in the flat
        dictionary may raise :exc:`RuntimeError` or fail to iterate over all
        entries.

        :rtype: Iterator
        :raises: RuntimeError

        """
        for item in self.items():
            yield item

    def iterkeys(self):
        """Iterate over the flat dictionary's keys. See the note for
        :meth:`flatdict.FlatDict.items`.

        Using ``iterkeys()`` while adding or deleting entries in the flat
        dictionary may raise :exc:`RuntimeError` or fail to iterate over all
        entries.

        :rtype: Iterator
        :raises: RuntimeError

        """
        for key in self.keys():
            yield key

    def itervalues(self):
        """Return an iterator over the flat dictionary's values. See the note
        :meth:`flatdict.FlatDict.items`.

        Using ``itervalues()`` while adding or deleting entries in the flat
        dictionary may raise a :exc:`RuntimeError` or fail to iterate over all
        entries.

        :rtype: Iterator
        :raises: RuntimeError

        """
        for value in self.values():
            yield value

    def keys(self):
        """Return a copy of the flat dictionary's list of keys.
        See the note for :meth:`flatdict.FlatDict.items`.

        :rtype: list

        """
        keys = []
        for key, value in self._values.items():
            if isinstance(value, (FlatDict, dict)):
                keys += [self._delimiter.join([key, k]) for k in value.keys()]
            else:
                keys.append(key)
        return sorted(keys)

    def pop(self, key, default=NO_DEFAULT):
        """If key is in the flat dictionary, remove it and return its value,
        else return default. If default is not given and key is not in the
        dictionary, :exc:`KeyError` is raised.

        :param mixed key: The key name
        :param mixed default: The default value
        :rtype: mixed

        """
        if key not in self and default != NO_DEFAULT:
            return default
        value = self[key]
        self.__delitem__(key)
        return value

    def setdefault(self, key, default):
        """If key is in the flat dictionary, return its value. If not,
        insert key with a value of default and return default.
        default defaults to ``None``.

        :param mixed key: The key name
        :param mixed default: The default value
        :rtype: mixed

        """
        if key not in self or not self.__getitem__(key):
            self.__setitem__(key, default)
        return self.__getitem__(key)

    def set_delimiter(self, delimiter):
        """Override the default or passed in delimiter with a new value. If
        the requested delimiter already exists in a key, a :exc:`ValueError`
        will be raised.

        :param str delimiter: The delimiter to use
        :raises: ValueError

        """
        for key in self.keys():
            if delimiter in key:
                raise ValueError('Key {!r} collides with delimiter {!r}', key,
                                 delimiter)
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

        :param iterable other: Iterable of key, value pairs
        :rtype: None

        """
        [self.__setitem__(k, v) for k, v in dict(other or kwargs).items()]

    def values(self):
        """Return a copy of the flat dictionary's list of values. See the note
        for :meth:`flatdict.FlatDict.items`.

        :rtype: list

        """
        return [self.__getitem__(k) for k in self.keys()]

    def _has_delimiter(self, key):
        """Checks to see if the key contains the delimiter.

        :rtype: bool

        """
        return isinstance(key, str) and self._delimiter in key


class FlatterDict(FlatDict):
    """Like :class:`~flatdict.FlatDict` but also coerces lists and sets
     to child-dict instances with the offset as the key. Alternative to
     the implementation added in v1.2 of FlatDict.

    """
    _COERCE = (list, tuple, set, dict, FlatDict)
    _ARRAYS = (list, set, tuple)

    def __init__(self, value=None, delimiter=':'):
        self.original_type = type(value)
        if self.original_type in self._ARRAYS:
            value = dict([(str(i), v) for i, v in enumerate(value)])
        super(FlatterDict, self).__init__(value, delimiter)

    def __setitem__(self, key, value):
        """Assign the value to the key, dynamically building nested
        FlatDict items where appropriate.

        :param mixed key: The key for the item
        :param mixed value: The value for the item
        :raises: TypeError

        """
        if isinstance(value, self._COERCE) and \
                not isinstance(value, FlatterDict):
            value = self.__class__(value, self._delimiter)
        if self._has_delimiter(key):
            pk, ck = key.split(self._delimiter, 1)
            if pk not in self._values:
                self._values[pk] = self.__class__({ck: value}, self._delimiter)
                return
            if getattr(self._values[pk],
                       'original_type', None) in self._ARRAYS:
                try:
                    int(ck)
                except ValueError:
                    raise TypeError(
                        'Assignment to invalid type for key {}{}{}'.format(
                            pk, self._delimiter, ck))
            elif not isinstance(self._values[pk], FlatterDict):
                raise TypeError(
                    'Assignment to invalid type for key {}'.format(pk))
            self._values[pk][ck] = value
        else:
            self._values[key] = value

    def as_dict(self):
        """Return the :class:`~flatdict.FlatterDict` as a nested
        :class:`dict`.

        :rtype: dict

        """
        out = dict({})
        for key in self.keys():
            if self._has_delimiter(key):
                pk, ck = key.split(self._delimiter, 1)
                if self._has_delimiter(ck):
                    ck = ck.split(self._delimiter, 1)[0]
                if isinstance(self._values[pk], FlatterDict) and pk not in out:
                    out[pk] = dict()
                if isinstance(self._values[pk][ck], FlatterDict):
                    if self._values[pk][ck].original_type == tuple:
                        out[pk][ck] = tuple(self._child_as_list(pk, ck))
                    elif self._values[pk][ck].original_type == list:
                        out[pk][ck] = self._child_as_list(pk, ck)
                    elif self._values[pk][ck].original_type == set:
                        out[pk][ck] = set(self._child_as_list(pk, ck))
                    elif self._values[pk][ck].original_type == dict:
                        out[pk][ck] = self._values[pk][ck].as_dict()
                else:
                    out[pk][ck] = self._values[pk][ck]
            else:
                out[key] = self._values[key]
        return out

    def _child_as_list(self, pk, ck):
        """Returns a list of values from the child FlatterDict instance
        with string based integer keys.

        :param str pk: The parent key
        :param str ck: The child key
        :rtype: list

        """
        return [self._values[pk][ck][k]
                for k in sorted(self._values[pk][ck].keys(),
                                key=lambda x: int(x))]
