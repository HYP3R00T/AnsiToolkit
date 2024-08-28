---
title: Effects
---
# Effects

The `Effects` class provides a collection of ANSI escape sequences to apply various text effects in the terminal, such as bold, italic, underline, and more. These effects are useful for enhancing the visual appearance of terminal output, allowing for better readability and emphasis in text-based applications.

## Usage

### Reset Effects

To reset all text formatting and effects to default:

```python
from ansitoolkit import Effects

# Reset all text effects
print(Effects.RESET)
```

### Apply Bold Effect

To make the text bold:

```python
# Apply bold effect to text
print(Effects.BOLD)
```

### Apply Dim Effect

To apply dim (faint) text effect:

```python
# Apply dim effect to text
print(Effects.DIM)
```

### Apply Italic Effect

To italicize the text:

```python
# Apply italic effect to text
print(Effects.ITALIC)
```

### Apply Underline Effect

To underline the text:

```python
# Apply underline effect to text
print(Effects.UNDERLINE)
```

### Apply Slow Blink Effect

To make the text blink slowly:

```python
# Apply slow blink effect to text
print(Effects.SLOW_BLINK)
```

### Apply Rapid Blink Effect

To make the text blink rapidly:

```python
# Apply rapid blink effect to text
print(Effects.RAPID_BLINK)
```

### Apply Reverse Video Effect

To reverse the text and background colors:

```python
# Apply reverse effect to text
print(Effects.REVERSE)
```

### Hide Text

To hide the text (make it invisible):

```python
# Hide the text
print(Effects.HIDE)
```

### Apply Strikethrough Effect

To strike through the text:

```python
# Apply strikethrough effect to text
print(Effects.STRIKETHROUGH)
```

### Apply Double Underline Effect

To apply a double underline to the text:

```python
# Apply double underline effect to text
print(Effects.DOUBLE_UNDERLINE)
```

### Reverting Effects

### Normal Intensity

To revert text to normal intensity (i.e., remove bold or dim effects):

```python
# Revert text to normal intensity
print(Effects.NORMAL_INTENSITY)
```

### Remove Italic Effect

To remove the italic effect from the text:

```python
# Remove italic effect from text
print(Effects.NOT_ITALIC)
```

### Remove Underline Effect

To remove the underline from the text:

```python
# Remove underline effect from text
print(Effects.NOT_UNDERLINED)
```

### Turn Off Blinking

To stop text from blinking:

```python
# Turn off blinking effect
print(Effects.BLINK_OFF)
```

### Turn Off Reverse Effect

To disable the reverse video effect:

```python
# Turn off reverse effect
print(Effects.REVERSE_OFF)
```

### Reveal Hidden Text

To reveal text that was previously hidden:

```python
# Reveal hidden text
print(Effects.REVEAL)
```

### Remove Strikethrough Effect

To remove the strikethrough effect from the text:

```python
# Remove strikethrough effect from text
print(Effects.NOT_STRIKETHROUGH)
```
