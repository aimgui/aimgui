import aimgui as gui

from imdemo.page import Page

class DrawTextPage(Page):
    def draw(self):
        gui.begin("Text")
        draw_list = gui.get_window_draw_list()
        draw_list.add_text((20, 35), gui.get_color_u32_rgba((1,1,0,1)), "Hello!")
        gui.end()

class TextPage(Page):
    def draw(self):
        gui.begin("Example: simple text")
        gui.text("Simple text")
        gui.end()

class ColoredTextPage(Page):
    def draw(self):
        gui.begin("Example: colored text")
        gui.text_colored((1, 0, 0, 1), "Colored text")
        gui.end()

class UnformattedTextPage(Page):
    def reset(self):
        self.text = '''
            Really ... 
            long ... 
            text
        '''

    def draw(self):
        gui.begin("Example: unformatted text")
        gui.text_unformatted(self.text)
        gui.end()

class LabelTextPage(Page):
    def draw(self):
        gui.begin("Example: text with label")
        gui.label_text("my label", "my text")
        gui.end()

def install(app):
    app.add_page(DrawTextPage, "drawtext", "Draw Text")
    app.add_page(TextPage, "text", "Text")
    app.add_page(ColoredTextPage, "coloredtext", "Colored Text")
    app.add_page(UnformattedTextPage, "unformattedtext", "Unformatted Text")
    app.add_page(LabelTextPage, "labeltext", "Text with Label")
