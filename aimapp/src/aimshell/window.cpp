#include "window.h"
#include "imgui.h"

void WindowBase::CreateContext() {
  IMGUI_CHECKVERSION();
  ImGui::CreateContext();
}
void WindowBase::DestroyContext() {
  ImGui::DestroyContext();
}

