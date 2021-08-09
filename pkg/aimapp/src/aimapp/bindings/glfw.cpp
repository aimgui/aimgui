#include <limits>

#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include <pybind11/stl.h>

#include <GLFW/glfw3.h>
struct GLFWmonitor { const char c; };
struct GLFWwindow { const char c; };
struct GLFWcursor { const char c; };

#include <aimgui/bindtools.h>

namespace py = pybind11;

void init_glfw(py::module &libaimapp, Registry &registry) {
    PYCLASS_BEGIN(libaimapp, GLFWvidmode, GLFWvidmode)
    GLFWvidmode.def_readwrite("width", &GLFWvidmode::width);
    GLFWvidmode.def_readwrite("height", &GLFWvidmode::height);
    GLFWvidmode.def_readwrite("red_bits", &GLFWvidmode::redBits);
    GLFWvidmode.def_readwrite("green_bits", &GLFWvidmode::greenBits);
    GLFWvidmode.def_readwrite("blue_bits", &GLFWvidmode::blueBits);
    GLFWvidmode.def_readwrite("refresh_rate", &GLFWvidmode::refreshRate);
    PYCLASS_END(libaimapp, GLFWvidmode, GLFWvidmode)

    PYCLASS_BEGIN(libaimapp, GLFWgammaramp, GLFWgammaramp)
    GLFWgammaramp.def_readwrite("red", &GLFWgammaramp::red);
    GLFWgammaramp.def_readwrite("green", &GLFWgammaramp::green);
    GLFWgammaramp.def_readwrite("blue", &GLFWgammaramp::blue);
    GLFWgammaramp.def_readwrite("size", &GLFWgammaramp::size);
    PYCLASS_END(libaimapp, GLFWgammaramp, GLFWgammaramp)

    PYCLASS_BEGIN(libaimapp, GLFWimage, GLFWimage)
    GLFWimage.def_readwrite("width", &GLFWimage::width);
    GLFWimage.def_readwrite("height", &GLFWimage::height);
    GLFWimage.def_readwrite("pixels", &GLFWimage::pixels);
    PYCLASS_END(libaimapp, GLFWimage, GLFWimage)

    PYCLASS_BEGIN(libaimapp, GLFWgamepadstate, GLFWgamepadstate)
    GLFWgamepadstate.def_readonly("buttons", &GLFWgamepadstate::buttons);
    GLFWgamepadstate.def_readonly("axes", &GLFWgamepadstate::axes);
    PYCLASS_END(libaimapp, GLFWgamepadstate, GLFWgamepadstate)

    libaimapp.def("glfw_init", &glfwInit
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_terminate", &glfwTerminate
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_init_hint", &glfwInitHint
    , py::arg("hint")
    , py::arg("value")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_version", [](int * major, int * minor, int * rev)
    {
        glfwGetVersion(major, minor, rev);
        return std::make_tuple(major, minor, rev);
    }
    , py::arg("major")
    , py::arg("minor")
    , py::arg("rev")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_version_string", &glfwGetVersionString
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_error", &glfwGetError
    , py::arg("description")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_monitors", [](int * count)
    {
        auto ret = glfwGetMonitors(count);
        return std::make_tuple(ret, count);
    }
    , py::arg("count")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_primary_monitor", &glfwGetPrimaryMonitor
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_monitor_pos", [](GLFWmonitor * monitor, int * xpos, int * ypos)
    {
        glfwGetMonitorPos(monitor, xpos, ypos);
        return std::make_tuple(xpos, ypos);
    }
    , py::arg("monitor")
    , py::arg("xpos")
    , py::arg("ypos")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_monitor_workarea", [](GLFWmonitor * monitor, int * xpos, int * ypos, int * width, int * height)
    {
        glfwGetMonitorWorkarea(monitor, xpos, ypos, width, height);
        return std::make_tuple(xpos, ypos, width, height);
    }
    , py::arg("monitor")
    , py::arg("xpos")
    , py::arg("ypos")
    , py::arg("width")
    , py::arg("height")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_monitor_physical_size", [](GLFWmonitor * monitor, int * widthMM, int * heightMM)
    {
        glfwGetMonitorPhysicalSize(monitor, widthMM, heightMM);
        return std::make_tuple(widthMM, heightMM);
    }
    , py::arg("monitor")
    , py::arg("width_mm")
    , py::arg("height_mm")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_monitor_content_scale", [](GLFWmonitor * monitor, float * xscale, float * yscale)
    {
        glfwGetMonitorContentScale(monitor, xscale, yscale);
        return std::make_tuple(xscale, yscale);
    }
    , py::arg("monitor")
    , py::arg("xscale")
    , py::arg("yscale")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_monitor_name", &glfwGetMonitorName
    , py::arg("monitor")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_set_monitor_user_pointer", &glfwSetMonitorUserPointer
    , py::arg("monitor")
    , py::arg("pointer")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_monitor_user_pointer", &glfwGetMonitorUserPointer
    , py::arg("monitor")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_video_modes", [](GLFWmonitor * monitor, int * count)
    {
        auto ret = glfwGetVideoModes(monitor, count);
        return std::make_tuple(ret, count);
    }
    , py::arg("monitor")
    , py::arg("count")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_video_mode", &glfwGetVideoMode
    , py::arg("monitor")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_set_gamma", &glfwSetGamma
    , py::arg("monitor")
    , py::arg("gamma")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_gamma_ramp", &glfwGetGammaRamp
    , py::arg("monitor")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_set_gamma_ramp", &glfwSetGammaRamp
    , py::arg("monitor")
    , py::arg("ramp")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_default_window_hints", &glfwDefaultWindowHints
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_window_hint", &glfwWindowHint
    , py::arg("hint")
    , py::arg("value")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_window_hint_string", &glfwWindowHintString
    , py::arg("hint")
    , py::arg("value")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_create_window", &glfwCreateWindow
    , py::arg("width")
    , py::arg("height")
    , py::arg("title")
    , py::arg("monitor")
    , py::arg("share")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_destroy_window", &glfwDestroyWindow
    , py::arg("window")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_window_should_close", &glfwWindowShouldClose
    , py::arg("window")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_set_window_should_close", &glfwSetWindowShouldClose
    , py::arg("window")
    , py::arg("value")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_set_window_title", &glfwSetWindowTitle
    , py::arg("window")
    , py::arg("title")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_set_window_icon", &glfwSetWindowIcon
    , py::arg("window")
    , py::arg("count")
    , py::arg("images")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_window_pos", [](GLFWwindow * window, int * xpos, int * ypos)
    {
        glfwGetWindowPos(window, xpos, ypos);
        return std::make_tuple(xpos, ypos);
    }
    , py::arg("window")
    , py::arg("xpos")
    , py::arg("ypos")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_set_window_pos", &glfwSetWindowPos
    , py::arg("window")
    , py::arg("xpos")
    , py::arg("ypos")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_window_size", [](GLFWwindow * window, int * width, int * height)
    {
        glfwGetWindowSize(window, width, height);
        return std::make_tuple(width, height);
    }
    , py::arg("window")
    , py::arg("width")
    , py::arg("height")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_set_window_size_limits", &glfwSetWindowSizeLimits
    , py::arg("window")
    , py::arg("minwidth")
    , py::arg("minheight")
    , py::arg("maxwidth")
    , py::arg("maxheight")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_set_window_aspect_ratio", &glfwSetWindowAspectRatio
    , py::arg("window")
    , py::arg("numer")
    , py::arg("denom")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_set_window_size", &glfwSetWindowSize
    , py::arg("window")
    , py::arg("width")
    , py::arg("height")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_framebuffer_size", [](GLFWwindow * window, int * width, int * height)
    {
        glfwGetFramebufferSize(window, width, height);
        return std::make_tuple(width, height);
    }
    , py::arg("window")
    , py::arg("width")
    , py::arg("height")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_window_frame_size", [](GLFWwindow * window, int * left, int * top, int * right, int * bottom)
    {
        glfwGetWindowFrameSize(window, left, top, right, bottom);
        return std::make_tuple(left, top, right, bottom);
    }
    , py::arg("window")
    , py::arg("left")
    , py::arg("top")
    , py::arg("right")
    , py::arg("bottom")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_window_content_scale", [](GLFWwindow * window, float * xscale, float * yscale)
    {
        glfwGetWindowContentScale(window, xscale, yscale);
        return std::make_tuple(xscale, yscale);
    }
    , py::arg("window")
    , py::arg("xscale")
    , py::arg("yscale")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_window_opacity", &glfwGetWindowOpacity
    , py::arg("window")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_set_window_opacity", &glfwSetWindowOpacity
    , py::arg("window")
    , py::arg("opacity")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_iconify_window", &glfwIconifyWindow
    , py::arg("window")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_restore_window", &glfwRestoreWindow
    , py::arg("window")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_maximize_window", &glfwMaximizeWindow
    , py::arg("window")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_show_window", &glfwShowWindow
    , py::arg("window")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_hide_window", &glfwHideWindow
    , py::arg("window")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_focus_window", &glfwFocusWindow
    , py::arg("window")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_request_window_attention", &glfwRequestWindowAttention
    , py::arg("window")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_window_monitor", &glfwGetWindowMonitor
    , py::arg("window")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_set_window_monitor", &glfwSetWindowMonitor
    , py::arg("window")
    , py::arg("monitor")
    , py::arg("xpos")
    , py::arg("ypos")
    , py::arg("width")
    , py::arg("height")
    , py::arg("refresh_rate")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_window_attrib", &glfwGetWindowAttrib
    , py::arg("window")
    , py::arg("attrib")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_set_window_attrib", &glfwSetWindowAttrib
    , py::arg("window")
    , py::arg("attrib")
    , py::arg("value")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_set_window_user_pointer", &glfwSetWindowUserPointer
    , py::arg("window")
    , py::arg("pointer")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_window_user_pointer", &glfwGetWindowUserPointer
    , py::arg("window")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_poll_events", &glfwPollEvents
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_wait_events", &glfwWaitEvents
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_wait_events_timeout", &glfwWaitEventsTimeout
    , py::arg("timeout")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_post_empty_event", &glfwPostEmptyEvent
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_input_mode", &glfwGetInputMode
    , py::arg("window")
    , py::arg("mode")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_set_input_mode", &glfwSetInputMode
    , py::arg("window")
    , py::arg("mode")
    , py::arg("value")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_raw_mouse_motion_supported", &glfwRawMouseMotionSupported
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_key_name", &glfwGetKeyName
    , py::arg("key")
    , py::arg("scancode")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_key_scancode", &glfwGetKeyScancode
    , py::arg("key")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_key", &glfwGetKey
    , py::arg("window")
    , py::arg("key")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_mouse_button", &glfwGetMouseButton
    , py::arg("window")
    , py::arg("button")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_cursor_pos", [](GLFWwindow * window, double * xpos, double * ypos)
    {
        glfwGetCursorPos(window, xpos, ypos);
        return std::make_tuple(xpos, ypos);
    }
    , py::arg("window")
    , py::arg("xpos")
    , py::arg("ypos")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_set_cursor_pos", &glfwSetCursorPos
    , py::arg("window")
    , py::arg("xpos")
    , py::arg("ypos")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_create_cursor", &glfwCreateCursor
    , py::arg("image")
    , py::arg("xhot")
    , py::arg("yhot")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_create_standard_cursor", &glfwCreateStandardCursor
    , py::arg("shape")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_destroy_cursor", &glfwDestroyCursor
    , py::arg("cursor")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_set_cursor", &glfwSetCursor
    , py::arg("window")
    , py::arg("cursor")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_joystick_present", &glfwJoystickPresent
    , py::arg("jid")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_joystick_axes", [](int jid, int * count)
    {
        auto ret = glfwGetJoystickAxes(jid, count);
        return std::make_tuple(ret, count);
    }
    , py::arg("jid")
    , py::arg("count")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_joystick_buttons", [](int jid, int * count)
    {
        auto ret = glfwGetJoystickButtons(jid, count);
        return std::make_tuple(ret, count);
    }
    , py::arg("jid")
    , py::arg("count")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_joystick_hats", [](int jid, int * count)
    {
        auto ret = glfwGetJoystickHats(jid, count);
        return std::make_tuple(ret, count);
    }
    , py::arg("jid")
    , py::arg("count")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_joystick_name", &glfwGetJoystickName
    , py::arg("jid")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_joystick_guid", &glfwGetJoystickGUID
    , py::arg("jid")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_set_joystick_user_pointer", &glfwSetJoystickUserPointer
    , py::arg("jid")
    , py::arg("pointer")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_joystick_user_pointer", &glfwGetJoystickUserPointer
    , py::arg("jid")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_joystick_is_gamepad", &glfwJoystickIsGamepad
    , py::arg("jid")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_update_gamepad_mappings", &glfwUpdateGamepadMappings
    , py::arg("string")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_gamepad_name", &glfwGetGamepadName
    , py::arg("jid")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_gamepad_state", &glfwGetGamepadState
    , py::arg("jid")
    , py::arg("state")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_set_clipboard_string", &glfwSetClipboardString
    , py::arg("window")
    , py::arg("string")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_clipboard_string", &glfwGetClipboardString
    , py::arg("window")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_time", &glfwGetTime
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_set_time", &glfwSetTime
    , py::arg("time")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_timer_value", &glfwGetTimerValue
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_timer_frequency", &glfwGetTimerFrequency
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_make_context_current", &glfwMakeContextCurrent
    , py::arg("window")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_get_current_context", &glfwGetCurrentContext
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_swap_buffers", &glfwSwapBuffers
    , py::arg("window")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_swap_interval", &glfwSwapInterval
    , py::arg("interval")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_extension_supported", &glfwExtensionSupported
    , py::arg("extension")
    , py::return_value_policy::automatic_reference);
    libaimapp.def("glfw_vulkan_supported", &glfwVulkanSupported
    , py::return_value_policy::automatic_reference);

}