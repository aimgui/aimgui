#pragma once

#include <functional>
#include <memory>
#include <string>

#include <windows.h>

#include <aimshell/glfw_window.h>

class Win32Window : public GlfwWindow {
 public:

  Win32Window();
  virtual ~Win32Window();
  virtual void Render() {}
  int AttachTo(HWND hParent);
  virtual bool PostCreate(WindowBase::CreateParams params) override;
  // Returns the backing Window handle to enable clients to set icon and other
  // window properties. Returns nullptr if the window has been destroyed.
  HWND GetHandle();

  // Return a RECT representing the bounds of the current client area.
  RECT GetClientArea();

};
