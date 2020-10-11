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

class DockingPage(Page):
    def reset(self):
        io = gui.get_io()
        io.config_flags |= gui.CONFIG_FLAGS_DOCKING_ENABLE
    def draw(self):
        #gui.begin(self.title, True, gui.WINDOW_FLAGS_DOCK_NODE_HOST)
        gui.begin(self.title, True)

        dockspace_id = gui.get_id(self.title)
        #ImGui::DockSpace(dockspaceID , ImVec2(0.0f, 0.0f), ImGuiDockNodeFlags_None|ImGuiDockNodeFlags_PassthruCentralNode/*|ImGuiDockNodeFlags_NoResize*/);
        #gui.dock_space(dockspace_id , gui.Vec2(0., 0.), gui.DOCK_NODE_FLAGS_NONE|gui.DOCK_NODE_FLAGS_PASSTHRU_CENTRAL_NODE)
        dockspace_flags = gui.DOCK_NODE_FLAGS_NONE|gui.DOCK_NODE_FLAGS_PASSTHRU_CENTRAL_NODE
        #dockspace_flags = gui.DOCK_NODE_FLAGS_NONE
        gui.dock_space(dockspace_id , (0., 0.), dockspace_flags)

        gui.end()


        #ImGui::SetNextWindowDockID(dockspaceID , ImGuiCond_FirstUseEver);
        gui.set_next_window_dock_id(dockspace_id , gui.COND_FIRST_USE_EVER)


        gui.begin('Dockable Window')
        gui.begin_child("region", (150, -50), border=True)
        gui.text("inside region")
        gui.end_child()
        gui.text("outside region")

def install(app):
    app.add_page(DockingPage, "docking", "Docking")
