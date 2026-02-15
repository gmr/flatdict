# Contributing

## Setting up a development environment

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and run:

```bash
uv sync
```

## Running Tests

```bash
uv run ruff check .
uv run ruff format --check .
uv run coverage run && uv run coverage report
```

`coverage xml` && `coverage html` are configured to output reports in the `build` directory.

## Test Coverage

To contribute to `flatdict`, please make sure that any new features or changes to existing functionality **include test coverage**.

*Pull requests that add or change code without coverage have a much lower chance of being accepted.*

**Pull requests that fail ruff checks as configured will not be accepted.**

## Code Formatting

Please format your code using [ruff](https://docs.astral.sh/ruff/)
prior to issuing your pull request.

## Versioning

flatdict subscribes to [semver](https://semver.org) style versioning.

Given a version number `MAJOR.MINOR.PATCH` increment the:

- `MAJOR` version when you make incompatible API changes,
- `MINOR` version when you add functionality in a backwards-compatible manner, and
- `PATCH` version when you make backwards-compatible bug fixes.
