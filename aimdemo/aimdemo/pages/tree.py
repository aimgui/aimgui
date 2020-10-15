import aimgui

from aimdemo.page import Page


class TreePage(Page):
    def draw(self):
        aimgui.begin(self.title)
        #if aimgui.tree_node("Expand me!", aimgui.TREE_NODE_DEFAULT_OPEN):
        if aimgui.tree_node("Expand me!"):
            aimgui.text("Lorem Ipsum")
            aimgui.tree_pop()
        aimgui.end()

def install(app):
    app.add_page(TreePage, "tree", "Tree")
