import arcade
import aimgui as gui

class Page(arcade.View):
    def __init__(self, window, name, title):
        super().__init__(window)
        self.window = window
        self.name = name
        self.title = title
        self.fullwidth = True
        self.fullheight = True

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

        #gui.set_next_window_pos((288, 32), gui.COND_ONCE)
        #gui.set_next_window_pos((self.window.width - 512 - 32, 32), gui.COND_ONCE)
        #gui.set_next_window_size((256, 512), gui.COND_ONCE)
        if self.fullwidth:
            x = self.window.width - (512+256) - 32
            width = 512
        else:
            x = self.window.width - (512) - 32
            width = 512/2

        if self.fullheight:
            y = 32
            height = self.window.height-32-16
        else:
            y = 32
            height = (self.window.height-32-16)/2

        #gui.set_next_window_pos((self.window.width - (512+256) - 32, 32), gui.COND_ONCE)
        #gui.set_next_window_size((512, self.window.height-32-16), gui.COND_ONCE)

        gui.set_next_window_pos((x, y), gui.COND_ONCE)
        gui.set_next_window_size((width, height), gui.COND_ONCE)

        self.draw()
        
        gui.end_frame()

    def draw_navbar(self):
        #gui.set_next_window_pos((16, 32), gui.COND_ONCE)
        gui.set_next_window_pos((self.window.width - 256 - 16, 32), gui.COND_ONCE)
        gui.set_next_window_size((256, self.window.height-32-16), gui.COND_ONCE)
        
        gui.begin("Examples")

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