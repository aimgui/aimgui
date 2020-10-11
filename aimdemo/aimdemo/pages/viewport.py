import aimgui as gui

from aimdemo.page import Page

'''
mGuiViewport* viewport = ImGui::GetMainViewport();
ImGui::SetNextWindowPos(viewport->Pos);
ImGui::SetNextWindowSize(viewport->Size);
ImGui::SetNextWindowViewport(viewport->ID);
ImGui::SetNextWindowBgAlpha(0.0f);

ImGuiWindowFlags window_flags = ImGuiWindowFlags_MenuBar | ImGuiWindowFlags_NoDocking;
window_flags |= ImGuiWindowFlags_NoTitleBar | ImGuiWindowFlags_NoCollapse | ImGuiWindowFlags_NoResize | ImGuiWindowFlags_NoMove;
window_flags |= ImGuiWindowFlags_NoBringToFrontOnFocus | ImGuiWindowFlags_NoNavFocus;

ImGui::PushStyleVar(ImGuiStyleVar_WindowRounding, 0.0f);
ImGui::PushStyleVar(ImGuiStyleVar_WindowBorderSize, 0.0f);
ImGui::PushStyleVar(ImGuiStyleVar_WindowPadding, ImVec2(0.0f, 0.0f));
ImGui::Begin("DockSpace Demo", p_open, window_flags);
ImGui::PopStyleVar(3);

ImGuiID dockspace_id = ImGui::GetID("MyDockspace");
ImGuiDockNodeFlags dockspace_flags = ImGuiDockNodeFlags_PassthruCentralNode;
ImGui::DockSpace(dockspace_id, ImVec2(0.0f, 0.0f), dockspace_flags);
'''

class ViewportPage(Page):
    def reset(self):
        io = gui.get_io()
        io.config_flags |= gui.CONFIG_FLAGS_DOCKING_ENABLE | gui.CONFIG_FLAGS_VIEWPORTS_ENABLE

    def draw(self):
        viewport = gui.get_main_viewport()
        gui.set_next_window_pos(viewport.pos)
        gui.set_next_window_size(viewport.size)
        gui.set_next_window_viewport(viewport.id)
        gui.set_next_window_bg_alpha(1)

        gui.begin(self.title)

        gui.begin_child("region", (150, -50), border=True)
        gui.text("inside region")
        gui.end_child()

        gui.text("outside region")
        gui.end()

def install(app):
    app.add_page(ViewportPage, "viewport", "Viewport")
