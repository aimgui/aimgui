import sys

from pyo import *

import arcade
import aimgui

def trim_docstring(docstring):
    if not docstring:
        return ''
    # Convert tabs to spaces (following the normal Python rules)
    # and split into a list of lines:
    lines = docstring.expandtabs().splitlines()
    # Determine minimum indentation (first line doesn't count):
    indent = sys.maxsize
    for line in lines[1:]:
        stripped = line.lstrip()
        if stripped:
            indent = min(indent, len(line) - len(stripped))
    # Remove indentation (first line is special):
    trimmed = [lines[0].strip()]
    if indent < sys.maxsize:
        for line in lines[1:]:
            trimmed.append(line[indent:].rstrip())
    # Strip off trailing and leading blank lines:
    while trimmed and not trimmed[-1]:
        trimmed.pop()
    while trimmed and not trimmed[0]:
        trimmed.pop(0)
    # Return a single string:
    return '\n'.join(trimmed)

class Page(arcade.View):
    def __init__(self, window, name, title):
        super().__init__(window)
        self.window = window
        self.name = name
        self.title = title
        self.fullwidth = True
        self.fullheight = True
        self.server = None

    @property
    def gui(self):
        return self.window.gui

    @property
    def resource_path(self):
        return self.window.resource_path

    def reset(self):
        if self.server:
            self.server.shutdown()
        self.create_server()
        self.gui.clear()
        self.do_reset()

    def do_reset(self):
        pass

    def start(self):
        self.start_server()
        self.do_start()

    def do_start(self):
        pass

    def create_server(self):
        self.server = s = Server(audio='jack')
        s.setMidiInputDevice(4)
        s.boot()

    def start_server(self):
        self.server.start()

    def stop(self):
        self.reset()

    def close(self):
        if self.server:
            self.server.shutdown()
        self.gui.clear()
        
    @classmethod
    def create(self, app, name, title):
        page = self(app, name, title)
        page.reset()
        return page

    def on_draw(self):
        arcade.start_render()

        aimgui.new_frame()
        
        if self.window.show_metrics:
            self.window.show_metrics = aimgui.show_metrics_window(True)

        if self.window.show_style_editor:
            self.window.show_style_editor = aimgui.begin('Style Editor', True)[1]
            aimgui.show_style_editor()
            aimgui.end()

        self.draw_mainmenu()
        self.draw_navbar()

        #gui.set_next_window_pos((288, 32), aimgui.COND_ONCE)
        #gui.set_next_window_pos((self.window.width - 512 - 32, 32), aimgui.COND_ONCE)
        #gui.set_next_window_size((256, 512), aimgui.COND_ONCE)
        if self.fullwidth:
            x = self.window.width - (512+256) - 32
            width = 512
        else:
            x = self.window.width - (512) - 32
            width = 512/2

        if self.fullheight:
            y = 32
            height = self.window.height-32-16
        else:
            y = 32
            height = (self.window.height-32-16)/2

        #gui.set_next_window_pos((self.window.width - (512+256) - 32, 32), aimgui.COND_ONCE)
        #gui.set_next_window_size((512, self.window.height-32-16), aimgui.COND_ONCE)

        aimgui.set_next_window_pos((x, y), aimgui.COND_ONCE)
        aimgui.set_next_window_size((width, height), aimgui.COND_ONCE)

        self.draw()
        self.window.gui.draw()
        aimgui.end_frame()

    def draw_navbar(self):
        aimgui.set_next_window_pos((self.window.width - 256 - 16, 32), aimgui.COND_ONCE)
        aimgui.set_next_window_size((256, self.window.height-32-16), aimgui.COND_ONCE)
        
        aimgui.begin("Examples")

        for section in self.window.sections.values():
            if aimgui.tree_node(section['title']):
                for entry in section['pages'].values():
                    opened, selected = aimgui.selectable(entry['title'], entry['name'] == self.window.page.name)
                    if opened:
                        self.window.show(entry['name'])
                aimgui.tree_pop()

        
        aimgui.end()

    def draw_mainmenu(self):
        if aimgui.begin_main_menu_bar():
            # File
            if aimgui.begin_menu('File', True):
                clicked_quit, selected_quit = aimgui.menu_item(
                    "Quit", 'Cmd+Q', False, True
                )

                if clicked_quit:
                    exit(1)

                aimgui.end_menu()
            # View
            if aimgui.begin_menu('View', True):
                clicked_metrics, self.window.show_metrics = aimgui.menu_item(
                    "Metrics", 'Cmd+M', self.window.show_metrics, True
                )
                clicked_metrics, self.window.show_style_editor = aimgui.menu_item(
                    "Style Editor", 'Cmd+S', self.window.show_style_editor, True
                )
                aimgui.end_menu()

            aimgui.end_main_menu_bar()

    def draw(self):
        aimgui.begin(self.title)

        if aimgui.button('Start'):
            self.start()
        if aimgui.button('Stop'):
            self.stop()

        if(self.__doc__):
            aimgui.text_unformatted(trim_docstring(self.__doc__))

        aimgui.end()
