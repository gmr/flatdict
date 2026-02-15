# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

FlatDict is a single-module Python library providing `FlatDict` and `FlatterDict` classes that flatten nested dictionaries into single-level dicts with delimited keys (e.g., `{"foo:bar": "baz"}`). `FlatterDict` additionally flattens lists, tuples, and sets. No runtime dependencies.

## Commands

```bash
# Setup dev environment
uv sync

# Run tests
uv run coverage run       # runs unittest discover under coverage
uv run coverage report    # print coverage summary

# Run a single test
uv run python -m unittest tests.FlatDictTests.test_method_name

# Lint
uv run ruff check .
uv run ruff format --check .
```

## Architecture

Package library — all code lives in `flatdict/__init__.py`, all tests in `tests.py`.

- `FlatDict(MutableMapping)` — core class, flattens nested dicts using a configurable delimiter (default `:`). Uses `maxsplit=1` on delimiter to resolve composite keys one level at a time.
- `FlatterDict(FlatDict)` — extends FlatDict to also flatten lists/tuples/sets using enumerated string indices, storing `original_type` to reconstruct via `as_dict()`.

## Lint/Style Config

Ruff config is in `pyproject.toml`.
