import arcade
import imgui
import imgui.core

from imdemo.page import Page


class TreePage(Page):
    def draw(self):
        imgui.begin(self.title)
        #if imgui.tree_node("Expand me!", imgui.TREE_NODE_DEFAULT_OPEN):
        if imgui.tree_node("Expand me!"):
            imgui.text("Lorem Ipsum")
            imgui.tree_pop()
        imgui.end()

def install(app):
    app.add_page(TreePage, "tree", "Tree")
