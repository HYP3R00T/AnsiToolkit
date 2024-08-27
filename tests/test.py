from ansitoolkit import (
    Colors,
    CursorMovement,
    DeviceStatus,
    Effects,
    GraphicsAndCharacterSets,
    KeyboardAndInputModes,
    ScreenControl,
    ScrollingRegion,
)


def test_colors():
    expected_fg_codes = {
        "FG_BLACK": "\033[30m",
        "FG_RED": "\033[31m",
        "FG_GREEN": "\033[32m",
        "FG_YELLOW": "\033[33m",
        "FG_BLUE": "\033[34m",
        "FG_MAGENTA": "\033[35m",
        "FG_CYAN": "\033[36m",
        "FG_WHITE": "\033[37m",
        "FG_BRIGHT_BLACK": "\033[90m",
        "FG_BRIGHT_RED": "\033[91m",
        "FG_BRIGHT_GREEN": "\033[92m",
        "FG_BRIGHT_YELLOW": "\033[93m",
        "FG_BRIGHT_BLUE": "\033[94m",
        "FG_BRIGHT_MAGENTA": "\033[95m",
        "FG_BRIGHT_CYAN": "\033[96m",
        "FG_BRIGHT_WHITE": "\033[97m",
    }

    expected_bg_codes = {
        "BG_BLACK": "\033[40m",
        "BG_RED": "\033[41m",
        "BG_GREEN": "\033[42m",
        "BG_YELLOW": "\033[43m",
        "BG_BLUE": "\033[44m",
        "BG_MAGENTA": "\033[45m",
        "BG_CYAN": "\033[46m",
        "BG_WHITE": "\033[47m",
        "BG_BRIGHT_BLACK": "\033[100m",
        "BG_BRIGHT_RED": "\033[101m",
        "BG_BRIGHT_GREEN": "\033[102m",
        "BG_BRIGHT_YELLOW": "\033[103m",
        "BG_BRIGHT_BLUE": "\033[104m",
        "BG_BRIGHT_MAGENTA": "\033[105m",
        "BG_BRIGHT_CYAN": "\033[106m",
        "BG_BRIGHT_WHITE": "\033[107m",
    }

    for color_name, expected_code in expected_fg_codes.items():
        assert getattr(Colors, color_name) == expected_code, f"{color_name} mismatch"

    for color_name, expected_code in expected_bg_codes.items():
        assert getattr(Colors, color_name) == expected_code, f"{color_name} mismatch"


def test_effects():
    assert Effects.RESET == "\033[0m"
    assert Effects.BOLD == "\033[1m"
    assert Effects.DIM == "\033[2m"
    assert Effects.ITALIC == "\033[3m"
    assert Effects.UNDERLINE == "\033[4m"
    assert Effects.SLOW_BLINK == "\033[5m"
    assert Effects.RAPID_BLINK == "\033[6m"
    assert Effects.REVERSE == "\033[7m"
    assert Effects.HIDE == "\033[8m"
    assert Effects.STRIKETHROUGH == "\033[9m"
    assert Effects.DOUBLE_UNDERLINE == "\033[21m"
    assert Effects.NORMAL_INTENSITY == "\033[22m"
    assert Effects.NOT_ITALIC == "\033[23m"
    assert Effects.NOT_UNDERLINED == "\033[24m"
    assert Effects.BLINK_OFF == "\033[25m"
    assert Effects.REVERSE_OFF == "\033[27m"
    assert Effects.REVEAL == "\033[28m"
    assert Effects.NOT_STRIKETHROUGH == "\033[29m"


def test_cursor_movement():
    assert CursorMovement.move_up(5) == "\033[5A"
    assert CursorMovement.move_down(3) == "\033[3B"
    assert CursorMovement.move_forward(7) == "\033[7C"
    assert CursorMovement.move_back(2) == "\033[2D"
    assert CursorMovement.move_next_line(4) == "\033[4E"
    assert CursorMovement.move_prev_line(1) == "\033[1F"
    assert CursorMovement.move_column(10) == "\033[10G"
    assert CursorMovement.move_position(5, 12) == "\033[5;12H"
    assert CursorMovement.RESET_POSITION == "\033[H"
    assert CursorMovement.SAVE_POSITION == "\033[s"
    assert CursorMovement.RESTORE_POSITION == "\033[u"


def test_screen_control():
    assert ScreenControl.CLEAR_ENTIRE_SCREEN == "\033[2J"
    assert ScreenControl.CLEAR_TO_END_OF_LINE == "\033[K"
    assert ScreenControl.CLEAR_TO_START_OF_LINE == "\033[1K"
    assert ScreenControl.CLEAR_ENTIRE_LINE == "\033[2K"
    assert ScreenControl.SHOW_CURSOR == "\033[?25h"
    assert ScreenControl.HIDE_CURSOR == "\033[?25l"
    assert ScreenControl.SWITCH_ALTERNATE_SCREEN == "\033[?1049h"
    assert ScreenControl.SWITCH_NORMAL_SCREEN == "\033[?1049l"


def test_scrolling_region():
    assert ScrollingRegion.set_scrolling_region(1, 10) == "\033[1;10r"
    assert ScrollingRegion.RESET_SCROLLING_REGION == "\033[0;0r"


def test_device_status():
    assert DeviceStatus.DEVICE_STATUS_REPORT == "\033[5n"
    assert DeviceStatus.TERMINAL_OK == "\033[0n"
    assert DeviceStatus.TERMINAL_MALFUNCTION == "\033[3n"
    assert DeviceStatus.CURSOR_POSITION_REPORT == "\033[6n"


def test_graphics_and_character_sets():
    assert GraphicsAndCharacterSets.STANDARD_MODE == "\033[0m"
    assert GraphicsAndCharacterSets.ENABLE_LINE_WRAPPING == "\033[?7h"
    assert GraphicsAndCharacterSets.DISABLE_LINE_WRAPPING == "\033[?7l"
    assert GraphicsAndCharacterSets.SET_CHARACTER_SET_G0 == "\033[11m"
    assert GraphicsAndCharacterSets.SET_CHARACTER_SET_G1 == "\033[12m"


def test_keyboard_and_input_modes():
    assert KeyboardAndInputModes.APPLICATION_KEYPAD_MODE == "\033[?1h"
    assert KeyboardAndInputModes.NORMAL_KEYPAD_MODE == "\033[?1l"
    assert KeyboardAndInputModes.ENABLE_CURSOR_VISIBILITY == "\033[?25h"
    assert KeyboardAndInputModes.DISABLE_CURSOR_VISIBILITY == "\033[?25l"
