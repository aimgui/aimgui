import arcade
import aimgui
import aimnodes

#from aimflo.wire import Wire
from aimflo.graph import Graph

class Page(arcade.View):
    def __init__(self, window, name, title):
        super().__init__(window)
        self.name = name
        self.title = title
        self.dragged = None
        self.graph = Graph()
        '''
        self.nodes = []
        self.node_map = {}
        self.wires = []
        self.wire_map = {}
        self.pin_map = {}
        '''
    
    def reset(self):
        self.graph.reset()
        '''
        for node in self.nodes:
            node.reset()
        '''
    '''
    def add_node(self, node):
        self.nodes.append(node)
        self.node_map[node.id] = node
        return node

    def remove_node(self, node):
        self.nodes.remove(node)
        self.node_map.pop(node.id)

    def add_wire(self, wire):
        self.wires.append(wire)
        self.wire_map[wire.id] = wire

    def remove_wire(self, wire):
        wire.destroy()
        self.wires.remove(wire)
        self.wire_map.pop(wire.id)

    def connect(self, output, input):
        self.add_wire(Wire(output, input))

    def disconnect(self, wire):
        self.remove_wire(wire)
    '''
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
        self.graph.update(delta_time)
        '''
        for node in self.nodes:
            node.update(delta_time)
        '''

    def on_draw(self):
      
        arcade.start_render()

        aimgui.new_frame()
        
        if self.window.show_metrics:
            self.window.show_metrics = aimgui.show_metrics_window(p_open=True)

        self.draw_mainmenu()
        self.draw_navbar()

        aimgui.set_next_window_pos((288, 32), aimgui.COND_ONCE)
        aimgui.set_next_window_size((512, 512), aimgui.COND_ONCE)

        self.draw()
        
        aimgui.end_frame()

    def draw_navbar(self):
        aimgui.set_next_window_pos((16, 32), aimgui.COND_ONCE)
        aimgui.set_next_window_size((256, self.window.height-32-16), aimgui.COND_ONCE)
        
        aimgui.begin("Examples")

        titles = [page['title'] for page in self.window.pages.values()]
        names = [page['name'] for page in self.window.pages.values()]

        if aimgui.begin_list_box("Examples", (-1, -1)):

            for entry in self.window.pages.values():
                opened, selected = aimgui.selectable(entry['title'], entry['name'] == self.window.page.name)
                if opened:
                    self.window.show(entry['name'])

            aimgui.end_list_box()
        
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
                clicked_metrics, self.window.show_metrics = aimgui.menu_item(
                    "Metrics", 'Cmd+M', self.window.show_metrics, True
                )

                aimgui.end_menu()

            aimgui.end_main_menu_bar()

    def draw(self):
        self.graph.draw()
        '''
        aimgui.begin('Node Editor')
        aimnodes.begin_node_editor()
        for node in self.nodes:
            node.draw()
        for wire in self.wires:
            wire.draw()
        aimnodes.end_node_editor()

        if (result := aimnodes.is_link_created(0,0))[0]:
            print(result)
            output = self.node_map[result[1]]
            input = self.node_map[result[2]]
            print('output:  {output}')
            print('input:  {input}')
            self.connect(output, input)

        if (result := aimnodes.is_link_destroyed(0))[0]:
            wire = self.wire_map[result[1]]
            print('destroyed: ', wire)
            self.disconnect(wire)

        aimgui.end()
        '''
