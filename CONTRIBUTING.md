# Contributing

## Setting up a development environment

Use of virtual environments will allow for isolated installation of testing requirements:

###Python 2

```bash
virtualenv -p python2.7 env27
source env/bin/activate
pip install -r test-requirements
```

###Python 3

```bash
python3 -m venv env
source env/bin/activate
pip install -r test-requirements
```

## Running Tests

###Python 2

```bash
source env27/bin/activate
./ci/test.sh
```

###Python 3

```bash
source env/bin/activate
./ci/test.sh
```

## Test Coverage

To contribute to `flatdict`, please make sure that any new features or changes to existing functionality **include test coverage**.

*Pull requests that add or change code without coverage have a much lower chance of being accepted.*

## Code Formatting

Please format your code using [yapf](http://pypi.python.org/pypi/yapf)
with ``pep8`` style prior to issuing your pull request.
