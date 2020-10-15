import aimgui

from aimdemo.page import Page


class Indent(Page):
    def draw(self):
        aimgui.begin("Example: item indenting")

        aimgui.text("Some text with bullets:")

        aimgui.bullet_text("Bullet A")
        aimgui.indent()
        aimgui.bullet_text("Bullet B (first indented)")
        aimgui.bullet_text("Bullet C (indent continues)")
        aimgui.unindent()
        aimgui.bullet_text("Bullet D (indent cleared)")

        aimgui.end()

def install(app):
    app.add_page(Indent, "indent", "Indent")

