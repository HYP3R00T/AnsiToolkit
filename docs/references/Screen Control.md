---
title: Screen Control
---
# ScreenControl

The `ScreenControl` class provides ANSI escape sequences for managing screen and cursor visibility in the terminal. These sequences allow you to clear parts of the screen, manage cursor visibility, and switch between different screen modes.

## Usage

### Clear to End of Screen

To clear the terminal screen from the current cursor position to the end of the screen:

```python
from ansitoolkit import ScreenControl

# Clear the screen from the cursor to the end
print(ScreenControl.CLEAR_TO_END_OF_SCREEN)
```

### Clear to Start of Screen

To clear the terminal screen from the current cursor position to the start of the screen:

```python
# Clear the screen from the cursor to the start
print(ScreenControl.CLEAR_TO_START_OF_SCREEN)
```

### Clear Entire Screen

To clear the entire terminal screen:

```python
# Clear the entire screen
print(ScreenControl.CLEAR_ENTIRE_SCREEN)
```

### Clear to End of Line

To clear the line from the current cursor position to the end of the line:

```python
# Clear from the cursor to the end of the line
print(ScreenControl.CLEAR_TO_END_OF_LINE)
```

### Clear to Start of Line

To clear the line from the current cursor position to the start of the line:

```python
# Clear from the cursor to the start of the line
print(ScreenControl.CLEAR_TO_START_OF_LINE)
```

### Clear Entire Line

To clear the entire line where the cursor is currently positioned:

```python
# Clear the entire line
print(ScreenControl.CLEAR_ENTIRE_LINE)
```

### Show Cursor

To make the cursor visible in the terminal:

```python
# Show the cursor
print(ScreenControl.SHOW_CURSOR)
```

### Hide Cursor

To hide the cursor in the terminal:

```python
# Hide the cursor
print(ScreenControl.HIDE_CURSOR)
```

### Switch to Alternate Screen

To switch to the alternate screen buffer, commonly used by text editors and other applications:

```python
# Switch to the alternate screen buffer
print(ScreenControl.SWITCH_ALTERNATE_SCREEN)
```

### Switch to Normal Screen

To switch back to the normal screen buffer:

```python
# Switch to the normal screen buffer
print(ScreenControl.SWITCH_NORMAL_SCREEN)
```
