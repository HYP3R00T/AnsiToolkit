---
title: Cursor Movement
---
# CursorMovement

The `CursorMovement` class provides a set of static methods to control cursor movement in the terminal using ANSI escape codes. These methods allow you to move the cursor up, down, forward, backward, and to specific positions, making it easier to format terminal output dynamically.

## Usage

### Moving the Cursor Up

To move the cursor up by a specific number of lines:

```python
from ansitoolkit import CursorMovement

# Move cursor up by 5 lines
print(CursorMovement.move_up(5))
```

### Moving the Cursor Down

To move the cursor down by a specific number of lines:

```python
# Move cursor down by 3 lines
print(CursorMovement.move_down(3))
```

### Moving the Cursor Forward

To move the cursor forward by a specific number of columns:

```python
# Move cursor forward by 10 columns
print(CursorMovement.move_forward(10))
```

### Moving the Cursor Backward

To move the cursor backward by a specific number of columns:

```python
# Move cursor back by 7 columns
print(CursorMovement.move_back(7))
```

### Moving to the Next Line

To move the cursor to the beginning of the next line:

```python
# Move to the next line 2 times
print(CursorMovement.move_next_line(2))
```

### Moving to the Previous Line

To move the cursor to the beginning of the previous line:

```python
# Move to the previous line 4 times
print(CursorMovement.move_prev_line(4))
```

### Moving to a Specific Column

To move the cursor to a specific column in the current line:

```python
# Move to column 15
print(CursorMovement.move_column(15))
```

### Moving to a Specific Position

To move the cursor to a specific row and column:

```python
# Move to row 10, column 20
print(CursorMovement.move_position(10, 20))
```

### Special Cursor Operations

### Resetting the Cursor Position

To reset the cursor to the home position (0,0):

```python
# Reset cursor to the top-left corner (home position)
print(CursorMovement.RESET_POSITION)
```

### Saving the Cursor Position

To save the current cursor position:

```python
# Save the current cursor position
print(CursorMovement.SAVE_POSITION)
```

### Restoring the Cursor Position

To restore the cursor to the previously saved position:

```python
# Restore the cursor to the saved position
print(CursorMovement.RESTORE_POSITION)
```
