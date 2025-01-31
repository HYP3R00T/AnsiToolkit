---
title: Cursor Shape
description: AnsiToolkit provides ANSI escape codes to control cursor shape, blinking, and behavior in terminal applications.
---
# CursorShape

The `CursorShape` class provides ANSI escape sequences for changing the appearance and behavior of the cursor in the terminal. These sequences allow you to control whether the cursor blinks, its shape (block, underline, or bar), and its steadiness.

## Usage

### Blinking Block Cursor

To set the cursor to a blinking block shape (the default in many terminals):

```python
from ansitoolkit import CursorShape

# Set cursor to blinking block
print(CursorShape.BLINKING_BLOCK)
```

### Steady Block Cursor

To set the cursor to a steady block shape (non-blinking):

```python
# Set cursor to steady block
print(CursorShape.STEADY_BLOCK)
```

### Blinking Underline Cursor

To set the cursor to a blinking underline shape:

```python
# Set cursor to blinking underline
print(CursorShape.BLINKING_UNDERLINE)
```

### Steady Underline Cursor

To set the cursor to a steady underline shape (non-blinking):

```python
# Set cursor to steady underline
print(CursorShape.STEADY_UNDERLINE)
```

### Blinking Bar Cursor

To set the cursor to a blinking bar shape (vertical bar):

```python
# Set cursor to blinking bar
print(CursorShape.BLINKING_BAR)
```

### Steady Bar Cursor

To set the cursor to a steady bar shape (non-blinking):

```python
# Set cursor to steady bar
print(CursorShape.STEADY_BAR)
```
