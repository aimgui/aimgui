#include <GLFW/glfw3.h>

#include "glfw_window.h"

static void glfw_error_callback(int error, const char* description)
{
    fprintf(stderr, "Glfw Error %d: %s\n", error, description);
}

GlfwWindow::GlfwWindow() {
}

GlfwWindow::~GlfwWindow() {
  Destroy();
}

//Event routing
void window_refresh_callback(GLFWwindow* win)
{
  GlfwWindow& window = *((GlfwWindow*)glfwGetWindowUserPointer(win));
  window.OnWindowRefresh();
}
void window_size_callback(GLFWwindow* win, int width, int height) {
  GlfwWindow& window = *((GlfwWindow*)glfwGetWindowUserPointer(win));
  window.OnWindowSize(width, height);
}
void window_pos_callback(GLFWwindow* win, int xpos, int ypos) {
  GlfwWindow& window = *((GlfwWindow*)glfwGetWindowUserPointer(win));
  window.OnWindowPos(xpos, ypos);
}
void window_cursor_pos_callback(GLFWwindow* win, double x, double y)
{
  GlfwWindow& window = *((GlfwWindow*)glfwGetWindowUserPointer(win));
  window.OnCursorPos(x, y);
}
void window_mouse_button_callback(GLFWwindow* win, int button, int action, int mods) {
  GlfwWindow& window = *((GlfwWindow*)glfwGetWindowUserPointer(win));
  window.OnMouseButton(button, action, mods);
}
void window_focus_callback(GLFWwindow* win, int focused) {
  GlfwWindow& window = *((GlfwWindow*)glfwGetWindowUserPointer(win));
  window.OnWindowFocus(focused);
}

bool GlfwWindow::DoCreate(CreateParams params) {
    // Setup window
    glfwSetErrorCallback(glfw_error_callback);
    if (!glfwInit())
        return false;

    // Create window with graphics context
    window_ = glfwCreateWindow(1280, 720, "Fausty!", NULL, NULL);
    if (window_ == NULL)
        return false;
    glfwMakeContextCurrent(window_);
    glfwSwapInterval(1); // Enable vsync

  return true;
}

bool GlfwWindow::PostCreate(CreateParams params) {
  glfwSetWindowUserPointer(window_, this);
  glfwSetWindowRefreshCallback(window_, window_refresh_callback);
  glfwSetWindowSizeCallback(window_, window_size_callback);
  glfwSetWindowPosCallback(window_, window_pos_callback);
  glfwSetCursorPosCallback(window_, window_cursor_pos_callback);
  glfwSetMouseButtonCallback(window_, window_mouse_button_callback);
  glfwSetWindowFocusCallback(window_, window_focus_callback);
  return WindowBase::PostCreate(params);
}

void GlfwWindow::SetQuitOnClose(bool quit_on_close) {
  quit_on_close_ = quit_on_close;
}

bool GlfwWindow::DoRun(RunParams params)
{

  GlfwWindow::Point origin(10, 10);
  GlfwWindow::Size size(1280, 720);
  bool success = CreateAndShow(CreateParams("NoName", origin, size));
  assert(success);
  if (!success) {
    return false;
  }
  // Main loop
  while (!glfwWindowShouldClose(window_))
  {
    glfwWaitEvents();
  }

  return WindowBase::DoRun(params);
}

bool GlfwWindow::PostRun(RunParams params) {
  Destroy();
  glfwTerminate();
  return WindowBase::PostRun(params);
}

void GlfwWindow::Destroy() {
  glfwDestroyWindow(window_);
  WindowBase::Destroy();
}