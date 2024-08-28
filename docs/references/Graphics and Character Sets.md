---
title: Graphics and CharacterSets
---
# GraphicsAndCharacterSets

The `GraphicsAndCharacterSets` class provides ANSI escape sequences for controlling various graphics and character set modes in the terminal. These sequences allow you to manage text wrapping, set character sets, and switch between different display modes.

## Usage

### Standard Mode

To switch to the standard graphics mode, which is typically the default mode:

```python
from ansitoolkit import GraphicsAndCharacterSets

# Switch to standard graphics mode
print(GraphicsAndCharacterSets.STANDARD_MODE)
```

### Enable Line Wrapping

To enable line wrapping, allowing text to wrap automatically at the end of a line:

```python
# Enable line wrapping
print(GraphicsAndCharacterSets.ENABLE_LINE_WRAPPING)
```

### Disable Line Wrapping

To disable line wrapping, so text does not automatically wrap and continues on a single line:

```python
# Disable line wrapping
print(GraphicsAndCharacterSets.DISABLE_LINE_WRAPPING)
```

### Set Character Set G0

To select the G0 character set, which is used for various standard text symbols and characters:

```python
# Set character set to G0
print(GraphicsAndCharacterSets.SET_CHARACTER_SET_G0)
```

### Set Character Set G1

To select the G1 character set, which is used for alternative symbols and characters:

```python
# Set character set to G1
print(GraphicsAndCharacterSets.SET_CHARACTER_SET_G1)
```
