# Changelog

<!-- changelogging: start -->

## 1.4.0 (2024-04-02)

- Added the following protocols:
  - `PartialLess[T]`;
  - `PartialGreater[T]`;
  - `PartialStrictOrdered[T]`;
  - `PartialLessOrEqual[T]`;
  - `PartialGreaterOrEqual[T]`;
  - `PartialLenientOrdered[T]`;
  - `PartialOrdered[T]`.

## 1.3.2 (2024-03-17)

### Features

- Added the `is_compare` function to check for items that implement the `Compare` protocol.

### Changes

- All the protocols in the library are now marked as `@runtime_checkable`.

## 1.3.1 (2024-02-26)

No significant changes.

## 1.3.0 (2024-02-24)

### Internal

- Dropped Python 3.7 support.
- Updated methods to use `(self, other: Self)` instead of `(self: T, other: T)`.

## 1.2.0 (2023-05-21)

### Internal

- Migrated to using `typing-aliases` library.

## 1.1.0 (2022-11-28)

### Fixes

- Added hints for type-checkers, showing that the `other` argument can be positional.

## 1.0.0 (2022-11-28)

Initial release.
