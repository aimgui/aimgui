import aimgui


class BaseOpenGLRenderer(object):
    def __init__(self):
        if not aimgui.get_current_context():
            raise RuntimeError(
                "No valid ImGui context. Use aimgui.create_context() first and/or "
                "aimgui.set_current_context()."
            )
        self.io = aimgui.get_io()

        self._font_texture = None

        self.io.delta_time = 1.0 / 60.0

        self._create_device_objects()
        self.refresh_font_texture()

    def render(self, draw_data):
        raise NotImplementedError

    def refresh_font_texture(self):
        raise NotImplementedError

    def _create_device_objects(self):
        raise NotImplementedError

    def _invalidate_device_objects(self):
        raise NotImplementedError

    def shutdown(self):
        self._invalidate_device_objects()
