import aimgui

from aimdemo.page import Page

OPTIONS = ["first", "second", "third"]

class ListboxPage(Page):
    def reset(self):
        self.options = OPTIONS
        self.current = 2

    def draw(self):    
        aimgui.begin(self.title)

        clicked, self.current = aimgui.list_box(
            "List", self.current, self.options
        )
        aimgui.text("selection: ")
        aimgui.same_line()
        aimgui.text(self.options[self.current])
        aimgui.end()

class CustomListboxPage(Page):
    def reset(self):
        self.selected = 'second'

    def draw(self):    
        aimgui.begin(self.title)

        if aimgui.list_box_header("Custom List", 200, 100):
            for option in OPTIONS:
                clicked, selected = aimgui.selectable(option, option == self.selected)
                if clicked:
                    self.selected = option

            aimgui.list_box_footer()

        aimgui.text("selection: ")
        aimgui.same_line()
        aimgui.text(self.selected)

        aimgui.end()

def install(app):
    app.add_page(ListboxPage, "listbox", "Listbox")
    app.add_page(CustomListboxPage, "customlistbox", "Listbox - Custom")
