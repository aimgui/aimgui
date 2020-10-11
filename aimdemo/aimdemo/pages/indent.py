import aimgui as gui

from aimdemo.page import Page


class Indent(Page):
    def draw(self):
        gui.begin("Example: item indenting")

        gui.text("Some text with bullets:")

        gui.bullet_text("Bullet A")
        gui.indent()
        gui.bullet_text("Bullet B (first indented)")
        gui.bullet_text("Bullet C (indent continues)")
        gui.unindent()
        gui.bullet_text("Bullet D (indent cleared)")

        gui.end()

def install(app):
    app.add_page(Indent, "indent", "Indent")

