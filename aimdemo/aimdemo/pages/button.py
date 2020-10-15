import aimgui

from aimdemo.page import Page


class Button(Page):
    def reset(self):
        self.message = ""

    def draw(self):
        aimgui.begin("Example: buttons")

        if aimgui.button("Button 1"):
            self.message = "You pressed 1!"
        if aimgui.button("Button 2"):
            self.message = "You pressed 2!"
        aimgui.text(self.message)
        aimgui.end()

RED = (1, 0, 0, 1)
GREEN = (0, 1, 0, 1)
BLUE = (0, 0, 1, 1)
MAGENTA = (1, 0, 1, 1)

class ColorButton(Page):
    def reset(self):
        self.color = (0,0,0,0)
        self.color_name = ''

    def draw(self):
        aimgui.begin("Example: color button")
        if aimgui.color_button("Button 1", RED, 0, (10, 10)):
            self.color = RED
            self.color_name = 'Red'
        if aimgui.color_button("Button 2", GREEN, 0, (10, 10)):
            self.color = GREEN
            self.color_name = 'Green'
        if aimgui.color_button("Wide Button", BLUE, 0, (20, 10)):
            self.color = BLUE
            self.color_name = 'Blue'
        if aimgui.color_button("Tall Button", MAGENTA, 0, (10, 20)):
            self.color = MAGENTA
            self.color_name = 'Magenta'
        #gui.text(f"You chose {self.color}")
        aimgui.text_colored(self.color, f"You chose {self.color_name}")
        aimgui.end()

class RadioButtonPage(Page):
    def reset(self):
        self.radio_active = True

    def draw(self):
        aimgui.begin(self.title)

        if aimgui.radio_button("Radio button", self.radio_active):
            self.radio_active = not self.radio_active

        aimgui.end()

def install(app):
    app.add_page(Button, "button", "Buttons")
    app.add_page(ColorButton, "colorbutton", "Buttons - Color")
    app.add_page(RadioButtonPage, "radiobutton", "Buttons - Radio")
