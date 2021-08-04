import arcade
import aimgui

class Wire:
    def __init__(self, output, input):
        self.input = input
        self.output = output
        input.add_wire(self)
        output.add_wire(self)

    def draw(self):
        pass
        '''
        x, y = self.output.get_position()
        x1, y1 = self.input.get_position()
        draw_list = aimgui.get_background_draw_list()
        #draw_list.add_line((x,y),(x1,y1), aimgui.get_color_u32((1,1,1,1)), 1)
        start = (x,y)
        end = (x1,y1)
        cp1 = (x+32, y)
        cp2 = (x1-32, y1)
        draw_list.add_bezier_cubic(start, cp1, cp2, end, aimgui.get_color_u32((1,1,1,1)), 1)
        '''