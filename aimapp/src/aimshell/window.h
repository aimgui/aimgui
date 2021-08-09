#pragma once

#include <string>
#include <thread>

#include "imgui.h"

class WindowBase {
public:
  struct Point {
    unsigned int x;
    unsigned int y;
    Point() {}
    Point(unsigned int x, unsigned int y) : x(x), y(y) {}
    Point(const Point& p1) { x = p1.x; y = p1.y; }
  };

  struct Size {
    unsigned int width;
    unsigned int height;
    Size() {}
    Size(unsigned int width, unsigned int height)
        : width(width), height(height) {}
    Size(const Size& s1) { width = s1.width; height = s1.height; }
  };
  //
  // Create
  //
  struct CreateParams {
    CreateParams(std::string _title = "No Name", Point _origin = Point(0,0), Size _size = Size(800,600)) {
      title = _title;
      origin = _origin;
      size = _size;
    }
    std::string title;
    Point origin;
    Size size;
  };

  bool Create(CreateParams params = CreateParams()) {
    if(!PreCreate(params)) { return false; }
    if(!DoCreate(params)) { return false; }
    if(!PostCreate(params)) { return false; }
    return true;
  }

  virtual bool PreCreate(CreateParams params){ return true; }
  virtual bool DoCreate(CreateParams params){ return true; }
  virtual bool PostCreate(CreateParams params){ return true; }

  bool CreateAndShow(CreateParams params = CreateParams()) {
    if(!Create(params)) { return false; }
    return Show();
  }
  virtual bool Show() { return true; }
  virtual bool Hide(){ return true; }
  /*
  * Context
  */
  virtual void CreateContext();
  virtual void DestroyContext();
  //
  // Destroy
  //
  virtual void Destroy() {}
  //
  // Run
  //
  struct RunParams {
    RunParams() {
    }
  };

  bool Run(RunParams params = RunParams()) {
    if (!PreRun(params)) { return false; }
    if (!DoRun(params)) { return false; }
    if (!PostRun(params)) { return false; }
    return true;
  }

  virtual bool PreRun(RunParams params) { return true; }
  virtual bool DoRun(RunParams params) { return true; }
  virtual bool PostRun(RunParams params) { return true; }

  //
  virtual void Render() {}
  virtual void Draw() {}
  // Events
  virtual void OnWindowRefresh() { Render(); }
  virtual void OnWindowSize(int width, int height) {}
  virtual void OnWindowPos(int xpos, int ypos) {}
  virtual void OnCursorPos(double x, double y) {}
  virtual void OnMouseButton(int button, int action, int mods) {}
  virtual void OnWindowFocus(int focused) {}

  // Data members
  std::thread paint_thread_;
  ImVec4 clear_color = ImVec4(0.45f, 0.55f, 0.60f, 1.00f);
};