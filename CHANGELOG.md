# Changelog

## 4.0.0 (2020-02-12)

- FIXED deprecation warning from Python 3.9 (#40 [nugend](https://github.com/nugend))
- FIXED keep order of received dict and it's nested objects (#38 [wsantos](https://github.com/wsantos))
- Drops Python 2 support and Python 3.4

## 3.4.0 (2019-07-24)

- FIXED sort order with regard to a nested list of dictionaries (#33 [wsantos](https://github.com/wsantos))

## 3.3.0 (2019-07-17)

- FIXED FlatDict.setdefault() to match dict behavior (#32 [abmyii](https://github.com/abmyii))
- FIXED empty nested Flatterdict (#30 [wsantos](https://github.com/wsantos))
- CHANGED functionality to allow setting and updating nests within iterables (#29 [mileslucas](https://github.com/mileslucas))

## 3.2.1 (2019-06-10)

- FIXED docs generation for readthedocs.io

## 3.2.0 (2019-06-10)

- FIXED List Flattening does not return list when an odd number of depth in the dictionary (#27 [mileslucas](https://github.com/mileslucas))
- CHANGED FlatterDict to allow for deeply nested dicts and lists when invoking `FlatterDict.as_dict()` (#28 [mileslucas](https://github.com/mileslucas))
- Flake8 cleanup/improvements
- Distribution/packaging updates to put metadata into setup.cfg

## 3.1.0 (2018-10-30)

- FIXED `FlatDict` behavior with empty iteratable values
- CHANGED behavior when casting to str or repr (#23)

## 3.0.1 (2018-07-01)

- Add 3.7 to Trove Classifiers
- Add Python 2.7 unicode string compatibility (#22 [nvllsvm](https://github.com/nvllsvm))

## 3.0.0 (2018-03-06)

- CHANGED `FlatDict.as_dict` to return the nested data structure based upon delimiters, coercing `FlatDict` objects to `dict`.
- CHANGED `FlatDict` to extend `collections.MutableMapping` instead of dict
- CHANGED `dict(FlatDict())` to return a shallow `dict` instance with the delimited keys as strings
- CHANGED `FlatDict.__eq__` to only evaluate against dict or the same class
- FIXED `FlatterDict` behavior to match expectations from pre-2.0 releases.

## 2.0.1 (2018-01-18)

- FIXED metadata for pypi upload

## 2.0.0 (2018-01-18)

- Code efficiency refactoring and cleanup
- Rewrote a majority of the tests, now at 100% coverage
- ADDED `FlatDict.__eq__` and `FlatDict.__ne__` (#13 - [arm77](https://github.com/arm77))
- ADDED `FlatterDict` class that performs the list, set, and tuple coercion that was added in v1.20
- REMOVED coercion of lists and tuples from `FlatDict` that was added in 1.2.0. Alternative to (#12 - [rj-jesus](https://github.com/rj-jesus))
- REMOVED `FlatDict.has_key()` as it duplicates of `FlatDict.__contains__`
- ADDED Python 3.5 and 3.6 to support matrix
- REMOVED support for Python 2.6 and Python 3.2, 3.3
- CHANGED `FlatDict.set_delimiter` to raise a `ValueError` if a key already exists with the delimiter value in it. (#8)

## 1.2.0 (2015-06-25)

- ADDED Support lists and tuples as well as dicts. (#4 - [alex-hutton](https://github.com/alex-hutton))

## 1.1.3 (2015-01-04)

- ADDED Python wheel support

## 1.1.2 (2013-10-09)

- Documentation and CI updates
- CHANGED use of `dict()` to a dict literal `{}`

## 1.1.1 (2012-08-17)

- ADDED `FlatDict.as_dict()`
- ADDED Python 3 support
- ADDED `FlatDict.set_delimiter()`
- Bugfixes and improvements from [naiquevin](https://github.com/naiquevin)

## 1.0.0 (2012-08-10)

- Initial release
