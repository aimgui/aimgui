__version__ = '0.1.0'

import sys
import platform
from pathlib import Path

version = platform.python_version_tuple()

LIB_PATH = Path(__file__).parent.parent / '_skbuild' / f"{platform.system().lower()}-{platform.machine()}-{version[0]}.{version[1]}" / "cmake-build"
print('LIB_PATH:  ', LIB_PATH)

sys.path.insert(0, str(LIB_PATH))
print(sys.path)

import libaimgui as core 
from libaimgui import *

from . import extra 
from aimgui.extra import *

VERTEX_BUFFER_POS_OFFSET = extra.vertex_buffer_vertex_pos_offset()
VERTEX_BUFFER_UV_OFFSET = extra.vertex_buffer_vertex_uv_offset()
VERTEX_BUFFER_COL_OFFSET = extra.vertex_buffer_vertex_col_offset()

VERTEX_SIZE = extra.vertex_buffer_vertex_size()
INDEX_SIZE = extra.index_buffer_index_size()

# ==== Condition constants (redefines for autodoc)
#: Set the variable always
ALWAYS = core.COND_ALWAYS
#: Only set the variable on the first call per runtime session
ONCE = core.COND_ONCE
#: Only set the variable if the window doesn't exist in the .ini file
FIRST_USE_EVER = core.COND_FIRST_USE_EVER
#: Only set the variable if the window is appearing after being inactive
#: (or the first time)
APPEARING = core.COND_APPEARING



# === Key map constants (redefines for autodoc)
#: for tabbing through fields
KEY_TAB = core.KEY_TAB
#: for text edit
KEY_LEFT_ARROW = core.KEY_LEFT_ARROW
#: for text edit
KEY_RIGHT_ARROW = core.KEY_RIGHT_ARROW
#: for text edit
KEY_UP_ARROW = core.KEY_UP_ARROW
#: for text edit
KEY_DOWN_ARROW = core.KEY_DOWN_ARROW
KEY_PAGE_UP = core.KEY_PAGE_UP
KEY_PAGE_DOWN = core.KEY_PAGE_DOWN
#: for text edit
KEY_HOME = core.KEY_HOME
#: for text edit
KEY_END = core.KEY_END
#: for text edit
KEY_INSERT = core.KEY_INSERT
#: for text edit
KEY_DELETE = core.KEY_DELETE
#: for text edit
KEY_BACKSPACE = core.KEY_BACKSPACE
#: for text edit
KEY_SPACE = core.KEY_SPACE
#: for text edit
KEY_ENTER = core.KEY_ENTER
#: for text edit
KEY_ESCAPE = core.KEY_ESCAPE
#: for text edit CTRL+A: select all
KEY_A = core.KEY_A
#: for text edit CTRL+C: copy
KEY_C = core.KEY_C
#: for text edit CTRL+V: paste
KEY_V = core.KEY_V
#: for text edit CTRL+X: cut
KEY_X = core.KEY_X
#: for text edit CTRL+Y: redo
KEY_Y = core.KEY_Y
#: for text edit CTRL+Z: undo
KEY_Z = core.KEY_Z


# === Style var constants (redefines for autodoc)
#: associated type: ``float``.
STYLE_ALPHA = core.STYLE_VAR_ALPHA
#: associated type: ``Vec2``.
STYLE_WINDOW_PADDING = core.STYLE_VAR_WINDOW_PADDING
#: associated type: ``float``.
STYLE_WINDOW_ROUNDING = core.STYLE_VAR_WINDOW_ROUNDING
#: associated type: ``float``.
STYLE_WINDOW_BORDERSIZE = core.STYLE_VAR_WINDOW_BORDER_SIZE
#: associated type: ``Vec2``.
STYLE_WINDOW_MIN_SIZE = core.STYLE_VAR_WINDOW_MIN_SIZE
#: associated type: ``Vec2``.
STYLE_WINDOW_TITLE_ALIGN = core.STYLE_VAR_WINDOW_TITLE_ALIGN
#: associated type: ``float``.
STYLE_CHILD_ROUNDING = core.STYLE_VAR_CHILD_ROUNDING
#: associated type: ``float``.
STYLE_CHILD_BORDERSIZE = core.STYLE_VAR_CHILD_BORDER_SIZE
#: associated type: ``float``.
STYLE_POPUP_ROUNDING = core.STYLE_VAR_POPUP_ROUNDING
#: associated type: ``float``.
STYLE_POPUP_BORDERSIZE = core.STYLE_VAR_POPUP_BORDER_SIZE
#: associated type: ``Vec2``.
STYLE_FRAME_PADDING = core.STYLE_VAR_FRAME_PADDING
#: associated type: ``float``.
STYLE_FRAME_ROUNDING = core.STYLE_VAR_FRAME_ROUNDING
#: associated type: ``float``.
STYLE_FRAME_BORDERSIZE = core.STYLE_VAR_FRAME_BORDER_SIZE
#: associated type: ``Vec2``.
STYLE_ITEM_SPACING = core.STYLE_VAR_ITEM_SPACING
#: associated type: ``Vec2``.
STYLE_ITEM_INNER_SPACING = core.STYLE_VAR_ITEM_INNER_SPACING
#: associated type: ``float``.
STYLE_INDENT_SPACING = core.STYLE_VAR_INDENT_SPACING
#: associated type: ``float``.
STYLE_SCROLLBAR_SIZE = core.STYLE_VAR_SCROLLBAR_SIZE
#: associated type: ``float``.
STYLE_SCROLLBAR_ROUNDING = core.STYLE_VAR_SCROLLBAR_ROUNDING
#: associated type: ``float``.
STYLE_GRAB_MIN_SIZE = core.STYLE_VAR_GRAB_MIN_SIZE
#: associated type: ``float``.
STYLE_GRAB_ROUNDING = core.STYLE_VAR_GRAB_ROUNDING
#: associated type: flags ImGuiAlign_*.
STYLE_BUTTON_TEXT_ALIGN = core.STYLE_VAR_BUTTON_TEXT_ALIGN

# === Window flag constants (redefines for autodoc)
#: Disable title-bar.
WINDOW_NO_TITLE_BAR = core.WINDOW_FLAGS_NO_TITLE_BAR
#: Disable user resizing with the lower-right grip.
WINDOW_NO_RESIZE = core.WINDOW_FLAGS_NO_RESIZE
#: Disable user moving the window.
WINDOW_NO_MOVE = core.WINDOW_FLAGS_NO_MOVE
#: Disable scrollbars (window can still scroll with mouse or programatically).
WINDOW_NO_SCROLLBAR = core.WINDOW_FLAGS_NO_SCROLLBAR
#: Disable user vertically scrolling with mouse wheel.
WINDOW_NO_SCROLL_WITH_MOUSE = core.WINDOW_FLAGS_NO_SCROLL_WITH_MOUSE
#: Disable user collapsing window by double-clicking on it.
WINDOW_NO_COLLAPSE = core.WINDOW_FLAGS_NO_COLLAPSE
#: Resize every window to its content every frame.
WINDOW_ALWAYS_AUTO_RESIZE = core.WINDOW_FLAGS_ALWAYS_AUTO_RESIZE
#: Never load/save settings in ``.ini`` file.
WINDOW_NO_SAVED_SETTINGS = core.WINDOW_FLAGS_NO_SAVED_SETTINGS
#: Disable catching mouse or keyboard inputs.
WINDOW_NO_INPUTS = core.WINDOW_FLAGS_NO_INPUTS
#: Has a menu-bar.
WINDOW_MENU_BAR = core.WINDOW_FLAGS_MENU_BAR
#: Allow horizontal scrollbar to appear (off by default).
WINDOW_HORIZONTAL_SCROLLBAR = core.WINDOW_FLAGS_HORIZONTAL_SCROLLBAR
#: Disable taking focus when transitioning from hidden to visible state.
WINDOW_NO_FOCUS_ON_APPEARING = core.WINDOW_FLAGS_NO_FOCUS_ON_APPEARING
#: Disable bringing window to front when taking focus (e.g. clicking on it or
#: programatically giving it focus).
WINDOW_NO_BRING_TO_FRONT_ON_FOCUS = core.WINDOW_FLAGS_NO_BRING_TO_FRONT_ON_FOCUS
#: Always show vertical scrollbar (even if ContentSize.y < Size.y).
WINDOW_ALWAYS_VERTICAL_SCROLLBAR = core.WINDOW_FLAGS_ALWAYS_VERTICAL_SCROLLBAR
#: Always show horizontal scrollbar (even if ContentSize.x < Size.x).
WINDOW_ALWAYS_HORIZONTAL_SCROLLBAR = core.WINDOW_FLAGS_ALWAYS_HORIZONTAL_SCROLLBAR
#: Ensure child windows without border uses style.WindowPadding (ignored by
#: default for non-bordered child windows, because more convenient).
WINDOW_ALWAYS_USE_WINDOW_PADDING = core.WINDOW_FLAGS_ALWAYS_USE_WINDOW_PADDING
# No gamepad/keyboard navigation within the window
WINDOW_NO_NAV_INPUTS = core.WINDOW_FLAGS_NO_NAV_INPUTS
# No focusing toward this window with gamepad/keyboard navigation
WINDOW_NO_NAV_FOCUS = core.WINDOW_FLAGS_NO_NAV_FOCUS
# Shortcut: ``imgui.WINDOW_NO_NAV_INPUTS | imgui.WINDOW_NO_NAV_FOCUS``.
WINDOW_NO_NAV = core.WINDOW_FLAGS_NO_NAV

# === Tree node flag constants (redefines for autodoc)
#: Draw as selected
TREE_NODE_SELECTED = core.TREE_NODE_FLAGS_SELECTED
#: Full colored frame (e.g. for :func:`imgui.core.collapsing_header`).
TREE_NODE_FRAMED = core.TREE_NODE_FLAGS_FRAMED
#: Hit testing to allow subsequent widgets to overlap this one
TREE_NODE_ALLOW_ITEM_OVERLAP = core.TREE_NODE_FLAGS_ALLOW_ITEM_OVERLAP
#: Don't do a ``TreePush()`` when open
#: (e.g. for :func:`imgui.core.collapsing_header`).
#: No extra indent nor pushing on ID stack.
TREE_NODE_NO_TREE_PUSH_ON_OPEN = core.TREE_NODE_FLAGS_NO_TREE_PUSH_ON_OPEN
#: Don't automatically and temporarily open node when Logging is active
#: (by default logging will automatically open tree nodes).
TREE_NODE_NO_AUTO_OPEN_ON_LOG = core.TREE_NODE_FLAGS_NO_AUTO_OPEN_ON_LOG
#: Default node to be open.
TREE_NODE_DEFAULT_OPEN = core.TREE_NODE_FLAGS_DEFAULT_OPEN
#: Need double-click to open node.
TREE_NODE_OPEN_ON_DOUBLE_CLICK = core.TREE_NODE_FLAGS_OPEN_ON_DOUBLE_CLICK
#: Only open when clicking on the arrow part. If
#: :py:data:`TREE_NODE_OPEN_ON_DOUBLE_CLICK` is also set,
#: single-click arrow or double-click all box to open.
TREE_NODE_OPEN_ON_ARROW = core.TREE_NODE_FLAGS_OPEN_ON_ARROW
#: No collapsing, no arrow (use as a convenience for leaf nodes).
TREE_NODE_LEAF = core.TREE_NODE_FLAGS_LEAF
#: Display a bullet instead of arrow.
TREE_NODE_BULLET = core.TREE_NODE_FLAGS_BULLET
#: Use FramePadding (even for an unframed text node) to vertically align
#: text baseline to regular widget height. Equivalent to calling
#: align_text_to_frame_padding()
TREE_NODE_FRAME_PADDING = core.TREE_NODE_FLAGS_FRAME_PADDING
#: Shortcut: ``imgui.TREE_NODE_FRAMED | imgui.TREE_NODE_NO_AUTO_OPEN_ON_LOG``.
TREE_NODE_COLLAPSING_HEADER = core.TREE_NODE_FLAGS_COLLAPSING_HEADER

# === Color flag constants (redefines for autodoc)
COLOR_TEXT = core.COL_TEXT
COLOR_TEXT_DISABLED = core.COL_TEXT_DISABLED
COLOR_WINDOW_BACKGROUND = core.COL_WINDOW_BG
COLOR_CHILD_BACKGROUND = core.COL_CHILD_BG
COLOR_POPUP_BACKGROUND = core.COL_POPUP_BG
COLOR_BORDER = core.COL_BORDER
COLOR_BORDER_SHADOW = core.COL_BORDER_SHADOW
COLOR_FRAME_BACKGROUND = core.COL_FRAME_BG
COLOR_FRAME_BACKGROUND_HOVERED = core.COL_FRAME_BG_HOVERED
COLOR_FRAME_BACKGROUND_ACTIVE = core.COL_FRAME_BG_ACTIVE
COLOR_TITLE_BACKGROUND = core.COL_TITLE_BG
COLOR_TITLE_BACKGROUND_ACTIVE = core.COL_TITLE_BG_ACTIVE
COLOR_TITLE_BACKGROUND_COLLAPSED = core.COL_TITLE_BG_COLLAPSED
COLOR_MENUBAR_BACKGROUND = core.COL_MENU_BAR_BG
COLOR_SCROLLBAR_BACKGROUND = core.COL_SCROLLBAR_BG
COLOR_SCROLLBAR_GRAB = core.COL_SCROLLBAR_GRAB
COLOR_SCROLLBAR_GRAB_HOVERED = core.COL_SCROLLBAR_GRAB_HOVERED
COLOR_SCROLLBAR_GRAB_ACTIVE = core.COL_SCROLLBAR_GRAB_ACTIVE
COLOR_CHECK_MARK = core.COL_CHECK_MARK
COLOR_SLIDER_GRAB = core.COL_SLIDER_GRAB
COLOR_SLIDER_GRAB_ACTIVE = core.COL_SLIDER_GRAB_ACTIVE
COLOR_BUTTON = core.COL_BUTTON
COLOR_BUTTON_HOVERED = core.COL_BUTTON_HOVERED
COLOR_BUTTON_ACTIVE = core.COL_BUTTON_ACTIVE
COLOR_HEADER = core.COL_HEADER
COLOR_HEADER_HOVERED = core.COL_HEADER_HOVERED
COLOR_HEADER_ACTIVE = core.COL_HEADER_ACTIVE
COLOR_SEPARATOR = core.COL_SEPARATOR
COLOR_SEPARATOR_HOVERED = core.COL_SEPARATOR_HOVERED
COLOR_SEPARATOR_ACTIVE = core.COL_SEPARATOR_ACTIVE
COLOR_RESIZE_GRIP = core.COL_RESIZE_GRIP
COLOR_RESIZE_GRIP_HOVERED = core.COL_RESIZE_GRIP_HOVERED
COLOR_RESIZE_GRIP_ACTIVE = core.COL_RESIZE_GRIP_ACTIVE
COLOR_PLOT_LINES = core.COL_PLOT_LINES
COLOR_PLOT_LINES_HOVERED = core.COL_PLOT_LINES_HOVERED
COLOR_PLOT_HISTOGRAM = core.COL_PLOT_HISTOGRAM
COLOR_PLOT_HISTOGRAM_HOVERED = core.COL_PLOT_HISTOGRAM_HOVERED
COLOR_TEXT_SELECTED_BACKGROUND = core.COL_TEXT_SELECTED_BG
COLOR_DRAG_DROP_TARGET = core.COL_DRAG_DROP_TARGET
COLOR_NAV_HIGHLIGHT = core.COL_NAV_HIGHLIGHT
COLOR_NAV_WINDOWING_HIGHLIGHT = core.COL_NAV_WINDOWING_HIGHLIGHT
COLOR_NAV_WINDOWING_DIM_BACKGROUND = core.COL_NAV_WINDOWING_DIM_BG
COLOR_MODAL_WINDOW_DIM_BACKGROUND = core.COL_MODAL_WINDOW_DIM_BG
COLOR_COUNT = core.COL_COUNT

# === Selectable flag constants (redefines for autodoc)
#: Clicking this don't close parent popup window.
SELECTABLE_DONT_CLOSE_POPUPS = core.SELECTABLE_FLAGS_DONT_CLOSE_POPUPS
#: Selectable frame can span all columns
#: (text will still fit in current column).
SELECTABLE_SPAN_ALL_COLUMNS = core.SELECTABLE_FLAGS_SPAN_ALL_COLUMNS
#: Generate press events on double clicks too.
SELECTABLE_ALLOW_DOUBLE_CLICK = core.SELECTABLE_FLAGS_ALLOW_DOUBLE_CLICK

# === Combo flag constants (redefines for autodoc)
#: Align the popup toward the left by default
COMBO_POPUP_ALIGN_LEFT = core.COMBO_FLAGS_POPUP_ALIGN_LEFT
#: Max ~4 items visible. Tip: If you want your combo popup to be a
#: specific size you can use SetNextWindowSizeConstraints() prior
#: to calling BeginCombo()
COMBO_HEIGHT_SMALL = core.COMBO_FLAGS_HEIGHT_SMALL
#: Max ~8 items visible (default)
COMBO_HEIGHT_REGULAR = core.COMBO_FLAGS_HEIGHT_REGULAR
#: Max ~20 items visible
COMBO_HEIGHT_LARGE = core.COMBO_FLAGS_HEIGHT_LARGE
#: As many fitting items as possible
COMBO_HEIGHT_LARGEST = core.COMBO_FLAGS_HEIGHT_LARGEST
#: Display on the preview box without the square arrow button
COMBO_NO_ARROW_BUTTON = core.COMBO_FLAGS_NO_ARROW_BUTTON
#: Display only a square arrow button
COMBO_NO_PREVIEW = core.COMBO_FLAGS_NO_PREVIEW
#: Shortcut: ``imgui.COMBO_HEIGHT_SMALL | imgui.COMBO_HEIGHT_REGULAR | imgui.COMBO_HEIGHT_LARGE | imgui.COMBO_HEIGHT_LARGEST``.
COMBO_HEIGHT_MASK = COMBO_HEIGHT_SMALL | COMBO_HEIGHT_REGULAR | COMBO_HEIGHT_LARGE | COMBO_HEIGHT_LARGEST

# === Focus flag constants (redefines for autodoc)
#: IsWindowFocused(): Return true if any children of the window is focused
FOCUS_CHILD_WINDOWS = core.FOCUSED_FLAGS_CHILD_WINDOWS
#: IsWindowFocused(): Test from root window (top most parent of the current hierarchy)
FOCUS_ROOT_WINDOW = core.FOCUSED_FLAGS_ROOT_WINDOW
#: IsWindowFocused(): Return true if any window is focused
FOCUS_ANY_WINDOW = core.FOCUSED_FLAGS_ANY_WINDOW
#: Shortcut: ``imgui.FOCUS_CHILD_WINDOWS | imgui.FOCUS_ROOT_WINDOW``.
FOCUS_ROOT_AND_CHILD_WINDOWS = core.FOCUSED_FLAGS_CHILD_WINDOWS | core.FOCUSED_FLAGS_ROOT_WINDOW

# === Hovered flag constants (redefines for autodoc)
#: Return true if directly over the item/window, not obstructed by
#: another window, not obstructed by an active popup or modal
#: blocking inputs under them.
HOVERED_NONE = core.HOVERED_FLAGS_NONE
#: IsWindowHovered() only: Return true if any children of the window is hovered
HOVERED_CHILD_WINDOWS = core.HOVERED_FLAGS_CHILD_WINDOWS
#: IsWindowHovered() only: Test from root window (top most parent of the current hierarchy)
HOVERED_ROOT_WINDOW = core.HOVERED_FLAGS_ROOT_WINDOW
#: IsWindowHovered() only: Return true if any window is hovered
HOVERED_ANY_WINDOW = core.HOVERED_FLAGS_ANY_WINDOW
#: Return true even if a popup window is normally blocking access to this item/window
HOVERED_ALLOW_WHEN_BLOCKED_BY_POPUP = core.HOVERED_FLAGS_ALLOW_WHEN_BLOCKED_BY_POPUP
#: Return true even if an active item is blocking access to this item/window. Useful for Drag and Drop patterns.
HOVERED_ALLOW_WHEN_BLOCKED_BY_ACTIVE_ITEM = core.HOVERED_FLAGS_ALLOW_WHEN_BLOCKED_BY_ACTIVE_ITEM
#: Return true even if the position is overlapped by another window
HOVERED_ALLOW_WHEN_OVERLAPPED = core.HOVERED_FLAGS_ALLOW_WHEN_OVERLAPPED
#: Shortcut: ``imgui.HOVERED_ALLOW_WHEN_BLOCKED_BY_POPUP | imgui.HOVERED_ALLOW_WHEN_BLOCKED_BY_ACTIVE_ITEM | imgui.HOVERED_ALLOW_WHEN_OVERLAPPED``.
HOVERED_RECT_ONLY = core.HOVERED_FLAGS_ALLOW_WHEN_BLOCKED_BY_POPUP | core.HOVERED_FLAGS_ALLOW_WHEN_BLOCKED_BY_ACTIVE_ITEM | core.HOVERED_FLAGS_ALLOW_WHEN_OVERLAPPED
#: Shortcut: ``imgui.HOVERED_ROOT_WINDOW | imgui.HOVERED_CHILD_WINDOWS``.
HOVERED_ROOT_AND_CHILD_WINDOWS = core.HOVERED_FLAGS_ROOT_WINDOW | core.HOVERED_FLAGS_CHILD_WINDOWS

# === Drag Drop flag constants (redefines for autodoc)
#: By default, a successful call to BeginDragDropSource opens a tooltip
#: so you can display a preview or description of the source contents.
#: This flag disable this behavior.
DRAG_DROP_SOURCE_NO_PREVIEW_TOOLTIP = core.DRAG_DROP_FLAGS_SOURCE_NO_PREVIEW_TOOLTIP
#: By default, when dragging we clear data so that IsItemHovered() will
#: return true, to avoid subsequent user code submitting tooltips. This
#: flag disable this behavior so you can still call IsItemHovered() on
#: the source item.
DRAG_DROP_SOURCE_NO_DISABLE_HOVER = core.DRAG_DROP_FLAGS_SOURCE_NO_DISABLE_HOVER
#: Disable the behavior that allows to open tree nodes and collapsing
#: header by holding over them while dragging a source item.
DRAG_DROP_SOURCE_NO_HOLD_TO_OPEN_OTHERS = core.DRAG_DROP_FLAGS_SOURCE_NO_HOLD_TO_OPEN_OTHERS
#: Allow items such as Text(), Image() that have no unique identifier to
#: be used as drag source, by manufacturing a temporary identifier based
#: on their window-relative position. This is extremely unusual within the
#: dear imgui ecosystem and so we made it explicit.
DRAG_DROP_SOURCE_ALLOW_NULL_ID = core.DRAG_DROP_FLAGS_SOURCE_ALLOW_NULL_ID
#: External source (from outside of imgui), won't attempt to read current
#: item/window info. Will always return true. Only one Extern source can
#: be active simultaneously.
DRAG_DROP_SOURCE_EXTERN = core.DRAG_DROP_FLAGS_SOURCE_EXTERN
#: Automatically expire the payload if the source cease to be submitted
#: (otherwise payloads are persisting while being dragged)
DRAG_DROP_SOURCE_AUTO_EXPIRE_PAYLOAD = core.DRAG_DROP_FLAGS_SOURCE_AUTO_EXPIRE_PAYLOAD

# === Accept Drag Drop Payload flag constants (redefines for autodoc)
#: AcceptDragDropPayload() will returns true even before the mouse button
#: is released. You can then call IsDelivery() to test if the payload
#: needs to be delivered.
DRAG_DROP_ACCEPT_BEFORE_DELIVERY = core.DRAG_DROP_FLAGS_ACCEPT_BEFORE_DELIVERY
#: Do not draw the default highlight rectangle when hovering over target.
DRAG_DROP_ACCEPT_NO_DRAW_DEFAULT_RECT = core.DRAG_DROP_FLAGS_ACCEPT_NO_DRAW_DEFAULT_RECT
#: For peeking ahead and inspecting the payload before delivery.
DRAG_DROP_ACCEPT_PEEK_ONLY = core.DRAG_DROP_FLAGS_ACCEPT_BEFORE_DELIVERY | core.DRAG_DROP_FLAGS_ACCEPT_NO_DRAW_DEFAULT_RECT
'''
# === Cardinal Direction
#: Direction None
DIRECTION_NONE = core.DIRECTION_NONE
#: Direction Left
DIRECTION_LEFT = core.DIRECTION_LEFT
#: Direction Right
DIRECTION_RIGHT = core.DIRECTION_RIGHT
#: Direction Up
DIRECTION_UP = core.DIRECTION_UP
#: Direction Down
DIRECTION_DOWN = core.DIRECTION_DOWN
'''
# === Mouse cursor flag constants (redefines for autodoc)
MOUSE_CURSOR_ARROW = core.MOUSE_CURSOR_ARROW
#: When hovering over InputText, etc.
MOUSE_CURSOR_TEXT_INPUT = core.MOUSE_CURSOR_TEXT_INPUT
#: Unused
MOUSE_CURSOR_RESIZE_ALL = core.MOUSE_CURSOR_RESIZE_ALL
#: When hovering over an horizontal border
MOUSE_CURSOR_RESIZE_NS = core.MOUSE_CURSOR_RESIZE_NS
#: When hovering over a vertical border or a column
MOUSE_CURSOR_RESIZE_EW = core.MOUSE_CURSOR_RESIZE_EW
#: When hovering over the bottom-left corner of a window
MOUSE_CURSOR_RESIZE_NESW = core.MOUSE_CURSOR_RESIZE_NESW
#: When hovering over the bottom-right corner of a window
MOUSE_CURSOR_RESIZE_NWSE = core.MOUSE_CURSOR_RESIZE_NWSE

# === Text input flag constants (redefines for autodoc)
#: Allow ``0123456789.+-*/``
INPUT_TEXT_CHARS_DECIMAL = core.INPUT_TEXT_FLAGS_CHARS_DECIMAL
#: Allow ``0123456789ABCDEFabcdef``
INPUT_TEXT_CHARS_HEXADECIMAL = core.INPUT_TEXT_FLAGS_CHARS_HEXADECIMAL
#: Turn a..z into A..Z
INPUT_TEXT_CHARS_UPPERCASE = core.INPUT_TEXT_FLAGS_CHARS_UPPERCASE
#: Filter out spaces, tabs
INPUT_TEXT_CHARS_NO_BLANK = core.INPUT_TEXT_FLAGS_CHARS_NO_BLANK
#: Select entire text when first taking mouse focus
INPUT_TEXT_AUTO_SELECT_ALL = core.INPUT_TEXT_FLAGS_AUTO_SELECT_ALL
#: Return 'true' when Enter is pressed (as opposed to when the
#: value was modified)
INPUT_TEXT_ENTER_RETURNS_TRUE = core.INPUT_TEXT_FLAGS_ENTER_RETURNS_TRUE
#: Call user function on pressing TAB (for completion handling)
INPUT_TEXT_CALLBACK_COMPLETION = core.INPUT_TEXT_FLAGS_CALLBACK_COMPLETION
#: Call user function on pressing Up/Down arrows (for history handling)
INPUT_TEXT_CALLBACK_HISTORY = core.INPUT_TEXT_FLAGS_CALLBACK_HISTORY
#: Call user function every time. User code may query cursor position,
#: modify text buffer.
INPUT_TEXT_CALLBACK_ALWAYS = core.INPUT_TEXT_FLAGS_CALLBACK_ALWAYS
#: Call user function to filter character. Modify data->EventChar to
#: replace/filter input, or return 1 to discard character.
INPUT_TEXT_CALLBACK_CHAR_FILTER = core.INPUT_TEXT_FLAGS_CALLBACK_CHAR_FILTER
#: Pressing TAB input a '\t' character into the text field
INPUT_TEXT_ALLOW_TAB_INPUT = core.INPUT_TEXT_FLAGS_ALLOW_TAB_INPUT
#: In multi-line mode, allow exiting edition by pressing Enter.
#: Ctrl+Enter to add new line (by default adds new lines with Enter).
INPUT_TEXT_CTRL_ENTER_FOR_NEW_LINE = core.INPUT_TEXT_FLAGS_CTRL_ENTER_FOR_NEW_LINE
#: Disable following the cursor horizontally
INPUT_TEXT_NO_HORIZONTAL_SCROLL = core.INPUT_TEXT_FLAGS_NO_HORIZONTAL_SCROLL
#: Insert mode
INPUT_TEXT_ALWAYS_INSERT_MODE = core.INPUT_TEXT_FLAGS_ALWAYS_INSERT_MODE
#: Read-only mode
INPUT_TEXT_READ_ONLY = core.INPUT_TEXT_FLAGS_READ_ONLY
#: Password mode, display all characters as '*'
INPUT_TEXT_PASSWORD = core.INPUT_TEXT_FLAGS_PASSWORD
#: Disable undo/redo. Note that input text owns the text data while
#: active, if you want to provide your own undo/redo stack you need
#: e.g. to call clear_active_id().
INPUT_TEXT_NO_UNDO_REDO = core.INPUT_TEXT_FLAGS_NO_UNDO_REDO
