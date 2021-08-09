#include <GLFW/glfw3.h>

#define GLFW_EXPOSE_NATIVE_WIN32
#include <GLFW/glfw3native.h>

#include "win32_window.h"

#include "resource.h"

Win32Window::Win32Window() {
}

Win32Window::~Win32Window() {
  Destroy();
}

RECT Win32Window::GetClientArea() {
  RECT frame;
  GetClientRect(GetHandle(), &frame);
  return frame;
}

HWND Win32Window::GetHandle() {
  return glfwGetWin32Window(window_);
}

int Win32Window::AttachTo(HWND hParent) {
  WindowBase::Point origin(10, 10);
  WindowBase::Size size(1280, 720);
  bool success = CreateAndShow(CreateParams("NoName", origin, size));
  assert(success);
  if (!success) {
    return 1;
  }
  HWND hWnd = GetHandle();
  SetParent(hWnd, hParent);
  const LONG nNewStyle = (GetWindowLong(hWnd, GWL_STYLE) & ~WS_POPUP & ~WS_OVERLAPPEDWINDOW) | WS_CHILDWINDOW | WS_VISIBLE;
  SetWindowLong(hWnd, GWL_STYLE, nNewStyle);
  const ULONG_PTR cNewStyle = GetClassLongPtr(hWnd, GCL_STYLE) | CS_DBLCLKS;
  SetClassLongPtr(hWnd, GCL_STYLE, cNewStyle);
  ShowWindow(hWnd, SW_NORMAL);

  return 0;
}

bool Win32Window::PostCreate(WindowBase::CreateParams params) {
  HWND hwnd = GetHandle();
  paint_thread_ = std::thread([hwnd]() {
    RECT rc;
    GetClientRect(hwnd, &rc);
    while (true) {
      std::this_thread::sleep_for(std::chrono::milliseconds(16));
      InvalidateRect(hwnd, &rc, true);
    }
    });

  return GlfwWindow::PostCreate(params);
}
