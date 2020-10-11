import aimgui as gui

from aimdemo.page import Page


class TreePage(Page):
    def draw(self):
        gui.begin(self.title)
        #if gui.tree_node("Expand me!", gui.TREE_NODE_DEFAULT_OPEN):
        if gui.tree_node("Expand me!"):
            gui.text("Lorem Ipsum")
            gui.tree_pop()
        gui.end()

def install(app):
    app.add_page(TreePage, "tree", "Tree")
