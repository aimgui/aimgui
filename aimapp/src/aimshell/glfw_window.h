#ifndef RUNNER_WIN32_WINDOW_H_
#define RUNNER_WIN32_WINDOW_H_

#include <functional>
#include <memory>
#include <string>

#include <faustyshell/window.h>

class GLFWwindow;

class GlfwWindow : public WindowBase {
 public:

  GlfwWindow();
  virtual ~GlfwWindow();
  virtual void Render() {}

  virtual bool DoCreate(CreateParams params) override;
  virtual bool PostCreate(CreateParams params) override;
  virtual bool DoRun(RunParams params) override;
  virtual bool PostRun(RunParams params) override;
  virtual void Destroy();
  // If true, closing this window will quit the application.
  void SetQuitOnClose(bool quit_on_close);

 protected:

  bool quit_on_close_ = false;
  //
  public:
  GLFWwindow* window_ = nullptr;
};

#endif  // RUNNER_WIN32_WINDOW_H_
