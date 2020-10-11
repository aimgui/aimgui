import aimgui as gui

from aimdemo.page import Page


class TextInputPage(Page):
    def reset(self):
        self.text_val = 'Type your message here.'

    def draw(self):
        gui.begin(self.title)
        changed, self.text_val = gui.input_text(
            'Text',
            self.text_val,
            256
        )
        gui.text('You wrote:')
        gui.same_line()
        gui.text(self.text_val)
        gui.end()

class MultiTextInputPage(Page):
    def reset(self):
        self.text_val = 'Type your message here.'

    def draw(self):
        gui.begin(self.title)
        changed, self.text_val = gui.input_text_multiline(
            'Message',
            self.text_val,
            2056
        )
        gui.text('You wrote:')
        gui.same_line()
        gui.text(self.text_val)
        gui.end()

def install(app):
    app.add_page(TextInputPage, "textinput", "Text Input")
    app.add_page(MultiTextInputPage, "multitextinput", "Multiline Text Input")
