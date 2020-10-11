import arcade
import aimgui as gui

class Page(arcade.View):
    def __init__(self, window, name, title):
        super().__init__(window)
        self.window = window
        self.name = name
        self.title = title

    def reset(self):
        pass

    @classmethod
    def create(self, app, name, title):
        page = self(app, name, title)
        page.reset()
        return page

    def on_draw(self):
        arcade.start_render()

        gui.new_frame()
        
        if self.window.view_metrics:
            self.window.view_metrics = gui.show_metrics_window(p_open=True)

        self.draw_mainmenu()
        self.draw_navbar()

        gui.set_next_window_pos((288, 32), gui.ONCE)
        gui.set_next_window_size((512, 512), gui.ONCE)

        self.draw()
        
        gui.end_frame()

    def draw_navbar(self):
        gui.set_next_window_pos((16, 32), gui.ONCE)
        gui.set_next_window_size((256, 732), gui.ONCE)
        
        gui.begin("Examples")

        titles = [page['title'] for page in self.window.pages.values()]
        names = [page['name'] for page in self.window.pages.values()]

        if gui.list_box_header("Examples", -1, -1):

            for entry in self.window.pages.values():
                opened, selected = gui.selectable(entry['title'], entry['name'] == self.window.page.name)
                if opened:
                    self.window.show(entry['name'])

            gui.list_box_footer()
        
        gui.end()

    def draw_mainmenu(self):
        if gui.begin_main_menu_bar():
            # File
            if gui.begin_menu('File', True):
                clicked_quit, selected_quit = gui.menu_item(
                    "Quit", 'Cmd+Q', False, True
                )

                if clicked_quit:
                    exit(1)

                gui.end_menu()
            # View
            if gui.begin_menu('View', True):
                clicked_metrics, self.window.view_metrics = gui.menu_item(
                    "Metrics", 'Cmd+M', self.window.view_metrics, True
                )

                gui.end_menu()

            gui.end_main_menu_bar()

    def draw(self):
        pass