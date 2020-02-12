# Contributing

## Setting up a development environment

Use of virtual environments will allow for isolated installation of testing requirements:

```bash
python3 -m venv env
source env/bin/activate
pip install -r test-requirements
```

## Running Tests

```bash
source env/bin/activate
flake8
coverage run -m unittest discover -v; coverage report -m
```

## Test Coverage

To contribute to `flatdict`, please make sure that any new features or changes to existing functionality **include test coverage**.

*Pull requests that add or change code without coverage have a much lower chance of being accepted.*

## Code Formatting

Please format your code using [yapf](http://pypi.python.org/pypi/yapf)
with ``pep8`` style prior to issuing your pull request.

## Versioning

flatdict subscribes to [semver](https://semver.org) style versioning.

Given a version number `MAJOR.MINOR.PATCH` increment the:

- `MAJOR` version when you make incompatible API changes,
- `MINOR` version when you add functionality in a backwards-compatible manner, and
- `PATCH` version when you make backwards-compatible bug fixes.
