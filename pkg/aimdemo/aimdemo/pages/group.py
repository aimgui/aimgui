import aimgui

from aimdemo.page import Page


class Group(Page):
    def draw(self):
        aimgui.begin("Example: item groups")

        aimgui.begin_group()
        aimgui.text("First group (buttons):")
        aimgui.button("Button A")
        aimgui.button("Button B")
        aimgui.end_group()

        aimgui.same_line(spacing=50)

        aimgui.begin_group()
        aimgui.text("Second group (text and bullet texts):")
        aimgui.bullet_text("Bullet A")
        aimgui.bullet_text("Bullet B")
        aimgui.end_group()

        aimgui.end()

def install(app):
    app.add_page(Group, "group", "Group")
