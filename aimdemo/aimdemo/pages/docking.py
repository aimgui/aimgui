import aimgui

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
        io = aimgui.get_io()
        io.config_flags |= aimgui.CONFIG_FLAGS_DOCKING_ENABLE
    def draw(self):
        #gui.begin(self.title, True, aimgui.WINDOW_FLAGS_DOCK_NODE_HOST)
        aimgui.begin(self.title, True)

        dockspace_id = aimgui.get_id(self.title)
        #ImGui::DockSpace(dockspaceID , ImVec2(0.0f, 0.0f), ImGuiDockNodeFlags_None|ImGuiDockNodeFlags_PassthruCentralNode/*|ImGuiDockNodeFlags_NoResize*/);
        #gui.dock_space(dockspace_id , aimgui.Vec2(0., 0.), aimgui.DOCK_NODE_FLAGS_NONE|aimgui.DOCK_NODE_FLAGS_PASSTHRU_CENTRAL_NODE)
        dockspace_flags = aimgui.DOCK_NODE_FLAGS_NONE|aimgui.DOCK_NODE_FLAGS_PASSTHRU_CENTRAL_NODE
        #dockspace_flags = aimgui.DOCK_NODE_FLAGS_NONE
        aimgui.dock_space(dockspace_id , (0., 0.), dockspace_flags)

        aimgui.end()


        #ImGui::SetNextWindowDockID(dockspaceID , ImGuiCond_FirstUseEver);
        aimgui.set_next_window_dock_id(dockspace_id , aimgui.COND_FIRST_USE_EVER)


        aimgui.begin('Dockable Window')
        aimgui.begin_child("region", (150, -50), border=True)
        aimgui.text("inside region")
        aimgui.end_child()
        aimgui.text("outside region")
        aimgui.end()

def install(app):
    app.add_page(DockingPage, "docking", "Docking")
