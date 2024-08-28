---
title: Scrolling Region
---
# ScrollingRegion

The `ScrollingRegion` class provides ANSI escape sequences for managing scrolling regions within the terminal. Scrolling regions allow you to define a specific area of the terminal that can scroll independently from the rest of the screen, which is useful for creating dynamic text displays or managing output in specific sections of the terminal.

## Usage Examples

### Set Scrolling Region

To define a scrolling region within the terminal from a specific top row to a bottom row. This allows you to create a windowed area where text can scroll while the rest of the terminal content remains static.

```python
from ansitoolkit import ScrollingRegion

# Define a scrolling region from row 5 to row 20
print(ScrollingRegion.set_scrolling_region(5, 20))
```

### Reset Scrolling Region

To reset the scrolling region to the default state, effectively disabling any previously set scrolling region:

```python
# Reset the scrolling region to default
print(ScrollingRegion.RESET_SCROLLING_REGION)
```
