# `orderings`

[![License][License Badge]][License]
[![Version][Version Badge]][Package]
[![Downloads][Downloads Badge]][Package]
[![Discord][Discord Badge]][Discord]

[![Documentation][Documentation Badge]][Documentation]
[![Check][Check Badge]][Actions]
[![Test][Test Badge]][Actions]
[![Coverage][Coverage Badge]][Coverage]

> *Ordering enumeration and protocols.*

## Installing

**Python 3.7 or above is required.**

### pip

Installing the library with `pip` is quite simple:

```console
$ pip install orderings
```

Alternatively, the library can be installed from source:

```console
$ git clone https://github.com/nekitdev/orderings.git
$ cd orderings
$ python -m pip install .
```

### poetry

You can add `orderings` as a dependency with the following command:

```console
$ poetry add orderings
```

Or by directly specifying it in the configuration like so:

```toml
[tool.poetry.dependencies]
orderings = "^1.1.0"
```

Alternatively, you can add it directly from the source:

```toml
[tool.poetry.dependencies.orderings]
git = "https://github.com/nekitdev/orderings.git"
```

## Examples

### Core

The core of `orderings` is the [`Ordering`][orderings.core.Ordering] enumeration
and the [`Compare`][orderings.core.Compare] protocol:

```python
from attrs import frozen
from orderings import Compare, Ordering

I = TypeVar("I", bound="Int")


@frozen()
class Int(Compare):
    value: int

    def compare(self: I, other: I) -> Ordering:
        self_value = self.value
        other_value = other.value

        if self_value < other_value:
            return Ordering.LESS

        if self_value > other_value:
            return Ordering.GREATER

        return Ordering.EQUAL
```

[`Compare`][orderings.core.Compare] implements all ordering operations
(`==`, `!=`, `<`, `>`, `<=`, `>=`) using the [`compare`][orderings.core.Compare.compare] method.

## Documentation

You can find the documentation [here][Documentation].

## Support

If you need support with the library, you can send an [email][Email]
or refer to the official [Discord server][Discord].

## Changelog

You can find the changelog [here][Changelog].

## Security Policy

You can find the Security Policy of `orderings` [here][Security].

## Contributing

If you are interested in contributing to `orderings`, make sure to take a look at the
[Contributing Guide][Contributing Guide], as well as the [Code of Conduct][Code of Conduct].

## License

`orderings` is licensed under the MIT License terms. See [License][License] for details.

[Email]: mailto:support@nekit.dev

[Discord]: https://nekit.dev/discord

[Actions]: https://github.com/nekitdev/orderings/actions

[Changelog]: https://github.com/nekitdev/orderings/blob/main/CHANGELOG.md
[Code of Conduct]: https://github.com/nekitdev/orderings/blob/main/CODE_OF_CONDUCT.md
[Contributing Guide]: https://github.com/nekitdev/orderings/blob/main/CONTRIBUTING.md
[Security]: https://github.com/nekitdev/orderings/blob/main/SECURITY.md

[License]: https://github.com/nekitdev/orderings/blob/main/LICENSE

[Package]: https://pypi.org/project/orderings
[Coverage]: https://codecov.io/gh/nekitdev/orderings
[Documentation]: https://nekitdev.github.io/orderings

[Discord Badge]: https://img.shields.io/badge/chat-discord-5865f2
[License Badge]: https://img.shields.io/pypi/l/orderings
[Version Badge]: https://img.shields.io/pypi/v/orderings
[Downloads Badge]: https://img.shields.io/pypi/dm/orderings

[Documentation Badge]: https://github.com/nekitdev/orderings/workflows/docs/badge.svg
[Check Badge]: https://github.com/nekitdev/orderings/workflows/check/badge.svg
[Test Badge]: https://github.com/nekitdev/orderings/workflows/test/badge.svg
[Coverage Badge]: https://codecov.io/gh/nekitdev/orderings/branch/main/graph/badge.svg

[orderings.core.Compare]: https://nekitdev.github.io/orderings/reference/core#orderings.core.Compare
[orderings.core.Compare.compare]: https://nekitdev.github.io/orderings/reference/core#orderings.core.Compare.compare
[orderings.core.Ordering]: https://nekitdev.github.io/orderings/reference/core#orderings.core.Ordering
