"""
This module provides extra utilities that are not part of core ImGui C++ API
but are useful in Python application.

"""

from contextlib import contextmanager

try:
    from itertools import izip_longest
except ImportError:
    from itertools import zip_longest as izip_longest

import libaimgui as core


__all__ = (
    "font",
    "styled",
    "istyled",
    "colored",
    "vertex_buffer_vertex_pos_offset",
    "vertex_buffer_vertex_uv_offset",
    "vertex_buffer_vertex_col_offset",
    "vertex_buffer_vertex_size",
    "index_buffer_index_size",
)

# === Extra utilities ====

@contextmanager
def font(font):
    """Use specified font in given context.

    .. visual-example::
        :auto_layout:
        :height: 100
        :width: 320

        io = imgui.get_io()

        new_font = io.fonts.add_font_from_file_ttf("DroidSans.ttf", 20)
        impl.refresh_font_texture()

        # later in frame code

        imgui.begin("Default Window")

        imgui.text("Text displayed using default font")
        with imgui.font(new_font):
            imgui.text("Text displayed using custom font")

        imgui.end()

    Args:
        font (_Font): font object retrieved from :any:`add_font_from_file_ttf`.
    """
    core.push_font(font)
    yield
    core.pop_font()


@contextmanager
def styled(variable, value):
    # note: we treat bool value as integer to guess if we are required to pop
    #       anything because IMGUI may simply skip pushing
    count = core.push_style_var(variable, value)
    yield
    core.pop_style_var(count)


@contextmanager
def colored(
    variable,
    r,
    g,
    b,
    a = 1.
):
    # note: we treat bool value as integer to guess if we are required to pop
    #       anything because IMGUI may simply skip pushing
    count = core.push_style_color(variable, r, g, b, a)
    yield
    core.pop_style_color(count)


@contextmanager
def istyled(variables_and_values):
    # todo: rename to nstyled?
    count = 0
    iterator = iter(variables_and_values)

    try:
        # note: this is a trick that allows us convert flat list to pairs
        for var, val in izip_longest(iterator, iterator, fillvalue=None):
            # note: since we group into pairs it is impossible to have
            #       var equal to None
            if val is not None:
                count += core.push_style_var(var, val)
            else:
                raise ValueError(
                    "Unsufficient style info: {} variable lacks a value"
                    "".format(var)
                )
    except:
        raise
    else:
        yield

    finally:
        # perf: short wiring despite we have a wrapper for this
        core.PopStyleVar(count)


@contextmanager
def scoped(str_id: str):
    """Use scoped ID within a block of code.

    This context manager can be used to distinguish widgets sharing
    same implicit identifiers without manual calling of :func:`push_id`
    :func:`pop_id` functions.

    Example:

    Args:
        str_id (str): ID to push and pop within marked scope
    """
    core.push_id(str_id)
    yield
    core.pop_id()

vertex_buffer_vertex_pos_offset = core._py_vertex_buffer_vertex_pos_offset
vertex_buffer_vertex_uv_offset = core._py_vertex_buffer_vertex_uv_offset
vertex_buffer_vertex_col_offset = core._py_vertex_buffer_vertex_col_offset
vertex_buffer_vertex_size = core._py_vertex_buffer_vertex_size
index_buffer_index_size = core._py_index_buffer_index_size
