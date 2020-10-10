import aimgui as gui

from imdemo.page import Page


class Group(Page):
    def draw(self):
        gui.begin("Example: item groups")

        gui.begin_group()
        gui.text("First group (buttons):")
        gui.button("Button A")
        gui.button("Button B")
        gui.end_group()

        gui.same_line(spacing=50)

        gui.begin_group()
        gui.text("Second group (text and bullet texts):")
        gui.bullet_text("Bullet A")
        gui.bullet_text("Bullet B")
        gui.end_group()

        gui.end()

def install(app):
    app.add_page(Group, "group", "Group")
