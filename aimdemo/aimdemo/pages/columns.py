import aimgui

from aimdemo.page import Page


class Columns(Page):
    def draw(self):
        aimgui.begin("Example: Columns - File list")
        aimgui.columns(4, 'fileList')
        aimgui.separator()
        aimgui.text("ID")
        aimgui.next_column()
        aimgui.text("File")
        aimgui.next_column()
        aimgui.text("Size")
        aimgui.next_column()
        aimgui.text("Last Modified")
        aimgui.next_column()
        aimgui.separator()
        aimgui.set_column_offset(1, 40)

        aimgui.next_column()
        aimgui.text('FileA.txt')
        aimgui.next_column()
        aimgui.text('57 Kb')
        aimgui.next_column()
        aimgui.text('12th Feb, 2016 12:19:01')
        aimgui.next_column()

        aimgui.next_column()
        aimgui.text('ImageQ.png')
        aimgui.next_column()
        aimgui.text('349 Kb')
        aimgui.next_column()
        aimgui.text('1st Mar, 2016 06:38:22')
        aimgui.next_column()

        aimgui.columns(1)
        aimgui.end()

def install(app):
    app.add_page(Columns, "columns", "Columns")
