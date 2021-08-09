import aimgui

from aimdemo.page import Page


class TextInputPage(Page):
    def reset(self):
        self.text_val = 'Type your message here.'

    def draw(self):
        aimgui.begin(self.title)
        changed, self.text_val = aimgui.input_text(
            'Text',
            self.text_val,
            256
        )
        aimgui.text('You wrote:')
        aimgui.same_line()
        aimgui.text(self.text_val)
        aimgui.end()

class MultiTextInputPage(Page):
    def reset(self):
        self.text_val = 'Type your message here.'

    def draw(self):
        aimgui.begin(self.title)
        changed, self.text_val = aimgui.input_text_multiline(
            'Message',
            self.text_val,
            2056,
            (0,0),
            0
        )
        aimgui.text('You wrote:')
        aimgui.same_line()
        aimgui.text(self.text_val)
        aimgui.end()

def install(app):
    app.add_page(TextInputPage, "textinput", "Text Input")
    app.add_page(MultiTextInputPage, "multitextinput", "Multiline Text Input")
