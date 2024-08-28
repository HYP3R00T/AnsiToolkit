---
title: Device Status
---
# DeviceStatus

The `DeviceStatus` class provides pre-defined ANSI escape sequences that allow you to query the status of the terminal, including device status, cursor position, and more. These sequences are useful when you need to interact with the terminal at a lower level, for tasks like checking the terminal's status or reporting its position.

## Usage

### Device Status Report

To send a device status report request to the terminal:

```python
from ansitoolkit import DeviceStatus

# Request a device status report
print(DeviceStatus.DEVICE_STATUS_REPORT)
```

### Terminal OK

To check if the terminal is functioning correctly:

```python
# Query if the terminal is OK
print(DeviceStatus.TERMINAL_OK)
```

### Terminal Malfunction

To check if the terminal is malfunctioning:

```python
# Query if the terminal is malfunctioning
print(DeviceStatus.TERMINAL_MALFUNCTION)
```

### Cursor Position Report

To request the current cursor position from the terminal:

```python
# Request the current cursor position
print(DeviceStatus.CURSOR_POSITION_REPORT)
```

### Query Device Attributes

To query the terminal for its attributes:

```python
# Query device attributes (e.g., terminal type)
print(DeviceStatus.QUERY_DEVICE_ATTRIBUTES)
```
