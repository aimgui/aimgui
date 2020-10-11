import aimgui as gui

from aimdemo.page import Page

lorem_ipsum = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
'''

class TabItem:
    def __init__(self, name, selected=True):
        self.name = name
        self.selected = selected
        self.visible = True
    def __enter__(self):
        self.selected, self.visible = gui.begin_tab_item(self.name, self.visible)
        return self
    def __exit__(self, type, value, traceback):
        gui.end_tab_item()

def tab_item(name, p_open):
    return TabItem(name, p_open)

class TabsPage(Page):
    def reset(self):
        self.tabs = [TabItem("Standard settings", True), TabItem("Render settings")]
        self.color = 1,1,1

    def draw(self):
        gui.begin(self.title)

        gui.begin_child("item view", (0, -gui.get_frame_height_with_spacing())) #Leave room for 1 line below us
        gui.text("Settings")
        gui.separator()

        if gui.begin_tab_bar("##Tabs"):
            with self.tabs[0] as t1:
                if t1.selected:
                    gui.text_wrapped(lorem_ipsum)

            with self.tabs[1] as t2:
                if t2.selected:
                    _, self.color = gui.color_picker3("Background color", self.color)

            gui.end_tab_bar()

        '''
        if gui.begin_tab_bar("##Tabs"):
            with tab_item("Standard settings", self.tabs[0]) as (result, p_open):
                if t1:
                    gui.text_wrapped(lorem_ipsum)

            with tab_item("Render settings", self.tabs[1]) as t2:
                if t2:
                    _, self.color = gui.color_picker3("Background color", self.color)

            gui.end_tab_bar()
        '''

        '''
        if gui.begin_tab_bar("##Tabs"):
            if gui.begin_tab_item("Standard settings", self.tabs[0]):
                gui.text_wrapped(lorem_ipsum)
                gui.end_tab_item()

            if gui.begin_tab_item("Render settings", self.tabs[1]):
                _, self.color = gui.color_picker3("Background color", self.color)
                gui.end_tab_item()

            gui.end_tab_bar()
        '''
        gui.end_child()

        gui.text("outside region")
        gui.end()

def install(app):
    app.add_page(TabsPage, "tabs2", "Tabs2")
