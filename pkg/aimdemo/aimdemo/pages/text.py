import aimgui
from aimgui import rel

from aimdemo.page import Page

class DrawTextPage(Page):
    def draw(self):
        aimgui.begin(self.title)
        draw_list = aimgui.get_window_draw_list()
        p1 = rel(100, 60)
        draw_list.add_text(p1, aimgui.get_color_u32((1,1,0,1)), "Hello!")
        aimgui.end()

class TextPage(Page):
    def draw(self):
        aimgui.begin(self.title)
        aimgui.text("Simple text")
        aimgui.end()

class ColoredTextPage(Page):
    def draw(self):
        aimgui.begin(self.title)
        aimgui.text_colored((1, 0, 0, 1), "Colored text")
        aimgui.end()

class UnformattedTextPage(Page):
    def reset(self):
        self.text = '''
            Really ... 
            long ... 
            text
        '''

    def draw(self):
        aimgui.begin(self.title)
        aimgui.text_unformatted(self.text)
        aimgui.end()

class LabelTextPage(Page):
    def draw(self):
        aimgui.begin(self.title)
        aimgui.label_text("my label", "my text")
        aimgui.end()

def install(app):
    app.add_page(DrawTextPage, "drawtext", "Draw Text")
    app.add_page(TextPage, "text", "Text")
    app.add_page(ColoredTextPage, "coloredtext", "Colored Text")
    app.add_page(UnformattedTextPage, "unformattedtext", "Unformatted Text")
    app.add_page(LabelTextPage, "labeltext", "Text with Label")
