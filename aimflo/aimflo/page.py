import arcade
import aimgui

from aimflo.wire import Wire

class Page(arcade.View):
    def __init__(self, window, name, title):
        super().__init__(window)
        self.name = name
        self.title = title
        self.dragged = None

        self.nodes = []
        self.wires = []

    def reset(self):
        for node in self.nodes:
            node.reset()

    def add_node(self, node):
        self.nodes.append(node)
        return node

    def connect(self, output, input):
        self.wires.append(Wire(output, input))

    @classmethod
    def create(self, app, name, title):
        page = self(app, name, title)
        page.reset()
        return page

    def start_dnd(self, dragged):
        self.dragged = dragged

    def end_dnd(self):
        dragged = self.dragged
        self.dragged = None
        return dragged

    def update(self, delta_time):
        for node in self.nodes:
            node.update(delta_time)

    def on_draw(self):
        arcade.start_render()

        aimgui.new_frame()
        
        if self.window.view_metrics:
            self.window.view_metrics = aimgui.show_metrics_window(p_open=True)

        self.draw_mainmenu()
        self.draw_navbar()

        aimgui.set_next_window_pos((288, 32), aimgui.COND_ONCE)
        aimgui.set_next_window_size((512, 512), aimgui.COND_ONCE)

        self.draw()
        
        aimgui.end_frame()

    def draw_navbar(self):
        aimgui.set_next_window_pos((16, 32), aimgui.COND_ONCE)
        aimgui.set_next_window_size((256, 732), aimgui.COND_ONCE)
        
        aimgui.begin("Examples")

        titles = [page['title'] for page in self.window.pages.values()]
        names = [page['name'] for page in self.window.pages.values()]

        if aimgui.list_box_header("Examples", -1, -1):

            for entry in self.window.pages.values():
                opened, selected = aimgui.selectable(entry['title'], entry['name'] == self.window.page.name)
                if opened:
                    self.window.show(entry['name'])

            aimgui.list_box_footer()
        
        aimgui.end()

    def draw_mainmenu(self):
        if aimgui.begin_main_menu_bar():
            # File
            if aimgui.begin_menu('File', True):
                clicked_quit, selected_quit = aimgui.menu_item(
                    "Quit", 'Cmd+Q', False, True
                )

                if clicked_quit:
                    exit(1)

                aimgui.end_menu()
            # View
            if aimgui.begin_menu('View', True):
                clicked_metrics, self.window.view_metrics = aimgui.menu_item(
                    "Metrics", 'Cmd+M', self.window.view_metrics, True
                )

                aimgui.end_menu()

            aimgui.end_main_menu_bar()

    def draw(self):
        for node in self.nodes:
            node.draw()

        for wire in self.wires:
            wire.draw()
