import aimgui as gui

from aimdemo.page import Page

OPTIONS = ["first", "second", "third"]

class ListboxPage(Page):
    def reset(self):
        self.options = OPTIONS
        self.current = 2

    def draw(self):    
        gui.begin(self.title)

        clicked, self.current = gui.list_box(
            "List", self.current, self.options
        )
        gui.text("selection: ")
        gui.same_line()
        gui.text(self.options[self.current])
        gui.end()

class CustomListboxPage(Page):
    def reset(self):
        self.selected = 'second'

    def draw(self):    
        gui.begin(self.title)

        if gui.list_box_header("Custom List", 200, 100):
            for option in OPTIONS:
                clicked, selected = gui.selectable(option, option == self.selected)
                if clicked:
                    self.selected = option

            gui.list_box_footer()

        gui.text("selection: ")
        gui.same_line()
        gui.text(self.selected)

        gui.end()

def install(app):
    app.add_page(ListboxPage, "listbox", "Listbox")
    app.add_page(CustomListboxPage, "customlistbox", "Listbox - Custom")
