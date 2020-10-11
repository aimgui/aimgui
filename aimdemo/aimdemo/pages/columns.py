import aimgui as gui

from aimdemo.page import Page


class Columns(Page):
    def draw(self):
        gui.begin("Example: Columns - File list")
        gui.columns(4, 'fileList')
        gui.separator()
        gui.text("ID")
        gui.next_column()
        gui.text("File")
        gui.next_column()
        gui.text("Size")
        gui.next_column()
        gui.text("Last Modified")
        gui.next_column()
        gui.separator()
        gui.set_column_offset(1, 40)

        gui.next_column()
        gui.text('FileA.txt')
        gui.next_column()
        gui.text('57 Kb')
        gui.next_column()
        gui.text('12th Feb, 2016 12:19:01')
        gui.next_column()

        gui.next_column()
        gui.text('ImageQ.png')
        gui.next_column()
        gui.text('349 Kb')
        gui.next_column()
        gui.text('1st Mar, 2016 06:38:22')
        gui.next_column()

        gui.columns(1)
        gui.end()

def install(app):
    app.add_page(Columns, "columns", "Columns")
