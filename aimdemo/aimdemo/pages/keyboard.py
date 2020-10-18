import aimgui

from aimdemo.page import Page


class KeyboardPage(Page):
    def draw(self):
        aimgui.begin(self.title)
        '''
        aimgui.label_text(str(aimgui.is_key_down()), "is down")
        aimgui.label_text(str(aimgui.get_key_index()), "index")
        aimgui.label_text(str(aimgui.is_key_pressed), "is pressed")
        aimgui.label_text(str(aimgui.is_key_released), "is released")
        '''
        aimgui.end()

def install(app):
    app.add_page(KeyboardPage, "keyboard", "Keyboard")
