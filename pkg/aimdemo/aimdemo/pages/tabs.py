import aimgui

from aimdemo.page import Page

lorem_ipsum = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
'''

'''
class TabItem:
    def __init__(self, name):
        self.name = name
        self.p_open = True
    def __enter__(self):
        self.value, self.p_open = aimgui.begin_tab_item(self.name, self.p_open)
        return self.value
    def __exit__(self, type, value, traceback):
        aimgui.end_tab_item()
'''

from contextlib import contextmanager

@contextmanager
def tab_item(name, p_open):
    result, p_open = aimgui.begin_tab_item(name, p_open)
    if not result:
        return
    try:
        yield p_open
    finally:
        aimgui.end_tab_item()

class TabsPage(Page):
    def reset(self):
        self.tabs = [True, True]
        self.color = 1,1,1

    def draw(self):
        aimgui.begin(self.title)

        aimgui.begin_child("item view", (0, -aimgui.get_frame_height_with_spacing())) #Leave room for 1 line below us
        aimgui.text("Settings")
        aimgui.separator()

        if aimgui.begin_tab_bar("##Tabs"):
            if aimgui.begin_tab_item("Standard settings", self.tabs[0])[0]:
                aimgui.text_wrapped(lorem_ipsum)
                aimgui.end_tab_item()

            if aimgui.begin_tab_item("Render settings", self.tabs[1])[0]:
                _, self.color = aimgui.color_picker3("Background color", self.color)
                aimgui.end_tab_item()

            aimgui.end_tab_bar()

        aimgui.end_child()

        aimgui.text("outside region")
        aimgui.end()

def install(app):
    app.add_page(TabsPage, "tabs", "Tabs")
