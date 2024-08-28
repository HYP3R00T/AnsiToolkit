---
title: Color
---

# Color

## Colors Class

The `Colors` class provides ANSI escape sequences for standard 8-bit colors, both for foreground and background purposes. These are predefined colors commonly used in terminals.

### Foreground Colors

Available colors:
- Black [`FG_BLACK`, `FG_BRIGHT_BLACK`]
- Red [`FG_RED`, `FG_BRIGHT_RED`]
- Green [`FG_GREEN`, `FG_BRIGHT_GREEN`]
- Yellow [`FG_YELLOW`, `FG_BRIGHT_YELLOW`]
- Blue [`FG_BLUE`, `FG_BRIGHT_BLUE`]
- Magenta [`FG_MAGENTA`, `FG_BRIGHT_MAGENTA`]
- Cyan [`FG_CYAN`, `FG_BRIGHT_CYAN`]
- White [`FG_WHITE`, `FG_BRIGHT_WHITE`]

```python
from ansitoolkit import Colors

# Set foreground color to red
print(Colors.FG_RED)
```

### Background Colors

Available colors:
- Black [`BG_BLACK`, `BG_BRIGHT_BLACK`]
- Red [`BG_RED`, `BG_BRIGHT_RED`]
- Green [`BG_GREEN`, `BG_BRIGHT_GREEN`]
- Yellow [`BG_YELLOW`, `BG_BRIGHT_YELLOW`]
- Blue [`BG_BLUE`, `BG_BRIGHT_BLUE`]
- Magenta [`BG_MAGENTA`, `BG_BRIGHT_MAGENTA`]
- Cyan [`BG_CYAN`, `BG_BRIGHT_CYAN`]
- White [`BG_WHITE`, `BG_BRIGHT_WHITE`]

```python
from ansitoolkit import Colors

# Set background color to blue
print(Colors.BG_BLUE)
```

## RGBColors Class

The `RGBColors` class allows for the use of true RGB colors in your terminal. You can specify any RGB values within the range of 0 to 255 for red, green, and blue.

### RGB Foreground

```python
from ansitoolkit import RGBColors

# Generate RGB foreground color sequence for color (255, 100, 50)
print(RGBColors.rgb_foreground(255, 100, 50))
```

### RGB Background

```python
from ansitoolkit import RGBColors

# Generate RGB background color sequence for color (50, 100, 200)
print(RGBColors.rgb_background(50, 100, 200))
```

**Range**: RGB values can be set between 0 and 255 for each color channel.

## Ansi256Colors Class

The `Ansi256Colors` class supports 256-color sequences, allowing for a broader range of colors compared to the basic 8-bit colors. You can specify a color index between 0 and 255.

### 256-Color Foreground

```python
from ansitoolkit import Ansi256Colors

# Set 256-color foreground color using index 123
print(Ansi256Colors.color_foreground(123))
```

### 256-Color Background

```python
from ansitoolkit import Ansi256Colors

# Set 256-color background color using index 45
print(Ansi256Colors.color_background(45))
```

**Range**: Color index values range from 0 to 255.

## HSLColors Class

The `HSLColors` class converts HSL (Hue, Saturation, Lightness) values into RGB and generates corresponding color sequences. This allows for colors based on the HSL color model.

### HSL Foreground

```python
from ansitoolkit import HSLColors

# Generate HSL foreground color sequence with hue=200, saturation=0.5, lightness=0.5
print(HSLColors.hsl_foreground(200, 0.5, 0.5))
```

### HSL Background

```python
from ansitoolkit import HSLColors

# Generate HSL background color sequence with hue=100, saturation=0.7, lightness=0.4
print(HSLColors.hsl_background(100, 0.7, 0.4))
```

**Range**:
- **Hue**: 0 to 360 degrees
- **Saturation**: 0 to 1
- **Lightness**: 0 to 1

## HexColors Class

The `HexColors` class enables the conversion of hex color codes to RGB and generating ANSI color sequences. This is useful for utilizing web color codes in terminal applications.

### Hex Foreground

```python
from ansitoolkit import HexColors

# Generate hex foreground color sequence for hex code "#ff5733"
print(HexColors.hex_foreground("#ff5733"))
```

### Hex Background

```python
from ansitoolkit import HexColors

# Generate hex background color sequence for hex code "#33ff57"
print(HexColors.hex_background("#33ff57"))
```

**Range**: Hex color codes must be 6 characters long, representing RGB values as hex digits.
