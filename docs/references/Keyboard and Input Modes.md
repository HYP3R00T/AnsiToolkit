---
title: Keyboard and Input Modes
---
# KeyboardAndInputModes

The `KeyboardAndInputModes` class provides ANSI escape sequences to manage keyboard and input modes in the terminal. These sequences control how the keypad operates and the visibility of the cursor, allowing for a more customized terminal interaction.

## Usage

### Application Keypad Mode

To switch the keypad to application mode, which is used by certain applications to interpret keypad inputs differently:

```python
from ansitoolkit import KeyboardAndInputModes

# Set keypad to application mode
print(KeyboardAndInputModes.APPLICATION_KEYPAD_MODE)
```

### Normal Keypad Mode

To switch the keypad back to normal mode, which is the default behavior for keypad inputs:

```python
# Set keypad to normal mode
print(KeyboardAndInputModes.NORMAL_KEYPAD_MODE)
```

### Enable Cursor Visibility

To make the cursor visible in the terminal:

```python
# Enable cursor visibility
print(KeyboardAndInputModes.ENABLE_CURSOR_VISIBILITY)
```

### Disable Cursor Visibility

To hide the cursor in the terminal:

```python
# Disable cursor visibility
print(KeyboardAndInputModes.DISABLE_CURSOR_VISIBILITY)
```
