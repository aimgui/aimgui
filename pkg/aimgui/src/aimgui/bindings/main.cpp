#include <limits>
#include <filesystem>
#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include <pybind11/stl.h>

#include "imgui.h"
#include "imgui_internal.h"

#include <aimgui/aimgui.h>
#include <aimgui/conversions.h>
#include <aimgui/bindtools.h>

namespace py = pybind11;

/*thread_local ImGuiContext* TImGui;
ImGuiContext* GetGImGui() {
  return TImGui;
}*/
ImGuiContext* TImGui;  // Current implicit context pointer

void init_main(py::module &_aimgui, Registry &registry) {
    template_ImVector<char>(_aimgui, "Vector_char");
    template_ImVector<float>(_aimgui, "Vector_float");
    template_ImVector<unsigned char>(_aimgui, "Vector_unsignedchar");
    template_ImVector<unsigned short>(_aimgui, "Vector_unsignedshort");
    template_ImVector<ImDrawCmd>(_aimgui, "Vector_DrawCmd");
    template_ImVector<ImDrawVert>(_aimgui, "Vector_DrawVert");
    template_ImVector<ImFontGlyph>(_aimgui, "Vector_FontGlyph");

    /*
        ImGuiContext needs to be an opaque type.  Wrap it with PyCapsule
    */
    //ImGuiContext* ImGui::CreateContext(ImFontAtlas* shared_font_atlas)
    _aimgui.def("create_context", [](ImFontAtlas* shared_font_atlas)
    {
        return py::capsule(ImGui::CreateContext(shared_font_atlas), "ImGuiContext");
    }
    , py::arg("shared_font_atlas") = nullptr
    , py::return_value_policy::automatic_reference);

    //void ImGui::DestroyContext(ImGuiContext* ctx)
    _aimgui.def("destroy_context", [](py::capsule& ctx)
    {
        ImGui::DestroyContext(ctx);
    }
    , py::arg("ctx") = nullptr
    , py::return_value_policy::automatic_reference);

    //ImGuiContext* ImGui::GetCurrentContext()
    _aimgui.def("get_current_context", []()
    {
        return (void*)ImGui::GetCurrentContext();
    }
    , py::return_value_policy::automatic_reference);

    //void ImGui::SetCurrentContext(ImGuiContext* ctx)
    _aimgui.def("set_current_context", [](py::capsule& ctx)
    {
        ImGui::SetCurrentContext(ctx);
    }
    , py::arg("ctx")
    , py::return_value_policy::automatic_reference);

    //bool ImGui::SetDragDropPayload(const char* type, const void* data, size_t data_size, ImGuiCond cond)
    _aimgui.def("set_drag_drop_payload", [](std::string type, std::string data, ImGuiCond cond)
    {
        return ImGui::SetDragDropPayload(type.c_str(), data.c_str(), data.length(), cond);
    }
    , py::arg("type")
    , py::arg("data")
    , py::arg("cond") = 0
    , py::return_value_policy::automatic_reference);

    _aimgui.def("get_vertex_buffer_vertex_pos_offset", []()
    {
        return offsetof(ImDrawVert, pos);
    }
    , py::return_value_policy::automatic_reference);
    _aimgui.def("get_vertex_buffer_vertex_uv_offset", []()
    {
        return offsetof(ImDrawVert, uv);
    }
    , py::return_value_policy::automatic_reference);
    _aimgui.def("get_vertex_buffer_vertex_col_offset", []()
    {
        return offsetof(ImDrawVert, col);
    }
    , py::return_value_policy::automatic_reference);
    _aimgui.def("get_vertex_buffer_vertex_size", []()
    {
        return AimDrawList::VERTEX_SIZE;
    }
    , py::return_value_policy::automatic_reference);
    _aimgui.def("get_index_buffer_index_size", []() {
        return AimDrawList::INDEX_SIZE;
    }
    , py::return_value_policy::automatic_reference);


    PYEXTEND_BEGIN(ImGuiStyle, Style)
    Style.def_property_readonly("colors", [](const ImGuiStyle &self) {
        auto colors = self.Colors;
        auto result = PyList_New(ImGuiCol_COUNT);
        for(int i = 0; i < ImGuiCol_COUNT; ++i ) {
            ImVec4 color = colors[i];
            auto item = PyTuple_New(4);
            PyTuple_SetItem(item, 0, PyFloat_FromDouble(color.x));
            PyTuple_SetItem(item, 1, PyFloat_FromDouble(color.y));
            PyTuple_SetItem(item, 2, PyFloat_FromDouble(color.z));
            PyTuple_SetItem(item, 3, PyFloat_FromDouble(color.w));
            PyList_SetItem(result, i, item);
        }
        return py::reinterpret_steal<py::list>(result);
    });
    Style.def("set_color", [](ImGuiStyle& self, int item, ImVec4 color)
    {
        if (item < 0) throw py::index_error();
        if (item >= IM_ARRAYSIZE(self.Colors)) throw py::index_error();
        self.Colors[item] = color;
    }, py::arg("item"), py::arg("color"));
    PYEXTEND_END

    PYEXTEND_BEGIN(ImGuiIO, IO)
    IO.def("set_mouse_down", [](ImGuiIO& self, int button, bool down)
    {
        if (button < 0) throw py::index_error();
        if (button >= IM_ARRAYSIZE(self.MouseDown)) throw py::index_error();
        self.MouseDown[button] = down;
    }, py::arg("button"), py::arg("down"));

    /*IO.def("set_key_down", [](ImGuiIO& self, int key, bool down)
    {
        if (key < 0) throw py::index_error();
        if (key >= IM_ARRAYSIZE(self.KeysDown)) throw py::index_error();
        self.KeysDown[key] = down;
    }, py::arg("key"), py::arg("down"));*/

    /*IO.def_property_readonly("key_map", [](const ImGuiIO &io) {
        auto result = PyList_New(ImGuiKey_COUNT);
        //auto keymap = ImGui::GetIO().KeyMap;
        auto keymap = io.KeyMap;
        for(int i = 0; i < ImGuiKey_COUNT; ++i ) {
            PyList_SetItem(result, i, PyLong_FromLong(keymap[i]));
        }
        //return list;
        return py::reinterpret_steal<py::object>(result);
    });*/

    /*IO.def("set_key_map", [](ImGuiIO& self, int key, int value)
    {
        if (key < 0) throw py::index_error();
        if (key >= IM_ARRAYSIZE(self.KeyMap)) throw py::index_error();
        self.KeyMap[key] = value;
    }, py::arg("key"), py::arg("value"));*/
    PYEXTEND_END

    PYEXTEND_BEGIN(ImDrawCmd, DrawCmd)
    DrawCmd.def_property("user_callback",
        [](const ImDrawCmd& self) {
            if(self.UserCallback.ptr() == nullptr) {
                return py::cast<py::object>(Py_None);
            } else {
                return py::object(self.UserCallback);
            }
        },
        [](ImDrawCmd& self, ImDrawCallback cb) {
            self.UserCallback = cb;
        }
    );
    PYEXTEND_END

    PYEXTEND_BEGIN(ImDrawList, DrawList)

    DrawList.def("add_callback", 
    [](ImDrawList &self ,ImDrawCallback callback, py::object callback_data) {
        return self.AddCallback(callback, callback_data.ptr());
    }
    , py::arg("callback")
    , py::arg("callback_data")
    , py::return_value_policy::automatic_reference);


    DrawList.def_property_readonly("cmd_buffer_size",
        [](const ImDrawList &dl) {
            auto result = PyLong_FromLong(dl.CmdBuffer.Size);
            return py::reinterpret_steal<py::object>(result);
        }
    );

    DrawList.def_property_readonly("cmd_buffer_data",
        [](const ImDrawList &dl) {
            auto result = PyMemoryView_FromMemory((char*)dl.CmdBuffer.Data, dl.CmdBuffer.Size*AimDrawList::COMMAND_SIZE, PyBUF_WRITE);
            return py::reinterpret_steal<py::object>(result);
        }
    );

    DrawList.def_property_readonly("vtx_buffer_size",
        [](const ImDrawList &dl) {
            auto result = PyLong_FromLong(dl.VtxBuffer.Size);
            return py::reinterpret_steal<py::object>(result);
        }
    );

    DrawList.def_property_readonly("vtx_buffer_data",
        [](const ImDrawList &dl) {
            auto result = PyMemoryView_FromMemory((char*)dl.VtxBuffer.Data, dl.VtxBuffer.Size*AimDrawList::VERTEX_SIZE, PyBUF_WRITE);
            return py::reinterpret_steal<py::object>(result);
        }
    );

    DrawList.def_property_readonly("idx_buffer_size",
        [](const ImDrawList &dl) {
            auto result = PyLong_FromLong(dl.IdxBuffer.Size);
            return py::reinterpret_steal<py::object>(result);
        }
    );

    DrawList.def_property_readonly("idx_buffer_data",
        [](const ImDrawList &dl) {
            auto result = PyMemoryView_FromMemory((char*)dl.IdxBuffer.Data, dl.IdxBuffer.Size*AimDrawList::INDEX_SIZE, PyBUF_WRITE);
            return py::reinterpret_steal<py::object>(result);
        }
    );

    DrawList.def("__iter__", 
        [](const ImDrawList &dl) { return py::make_iterator(dl.CmdBuffer.Data, dl.CmdBuffer.Data + dl.CmdBuffer.Size); },
        py::keep_alive<0, 1>() /* Essential: keep object alive while iterator exists */);

    //void ImDrawList::AddPolyline(const ImVec2* points, const int points_count, ImU32 col, bool closed, float thickness)
    DrawList.def("add_polyline",  [](ImDrawList& self, py::list points, ImU32 col, bool closed, float thickness)
    {
        const int points_count = points.size();
        ImVec2 *pts = (ImVec2*)malloc(points_count * sizeof(ImVec2));
        for(int i = 0; i < points_count; ++i) {
            py::object obj = points[i];
            pts[i] = obj.cast<ImVec2>();
        }
        self.AddPolyline(pts, points_count, col, closed, thickness);
        free(pts);
    }
    , py::arg("points")
    , py::arg("col")
    , py::arg("closed")
    , py::arg("thickness")
    , py::return_value_policy::automatic_reference);

    PYEXTEND_END

    PYEXTEND_BEGIN(ImDrawData, DrawData)
    DrawData.def_property_readonly("cmd_lists", [](const ImDrawData& self)
    {
        py::list ret;
        for(int i = 0; i < self.CmdListsCount; i++)
        {
            ret.append(self.CmdLists[i]);
        }
        return ret;
    });
    PYEXTEND_END

    PYEXTEND_BEGIN(ImDrawVert, DrawVert)
    DrawVert.def_property_readonly_static("pos_offset", [](py::object)
    {
        return IM_OFFSETOF(ImDrawVert, pos);
    });
    DrawVert.def_property_readonly_static("uv_offset", [](py::object)
    {
        return IM_OFFSETOF(ImDrawVert, uv);
    });
    DrawVert.def_property_readonly_static("col_offset", [](py::object)
    {
        return IM_OFFSETOF(ImDrawVert, col);
    });
    PYEXTEND_END

    PYEXTEND_BEGIN(ImFontAtlas, FontAtlas)
    //ImFont* ImFontAtlas::AddFontFromFileTTF(const char* filename, float size_pixels, const ImFontConfig* font_cfg_template, const ImWchar* glyph_ranges)
    //FontAtlas.def("add_font_from_file_ttf", [](ImFontAtlas& self, std::string filename, float size_pixels, const ImFontConfig* font_cfg_template, const ImWchar* glyph_ranges)
    FontAtlas.def("add_font_from_file_ttf", [](ImFontAtlas& self, std::string filename, float size_pixels)
    {
        //return self.AddFontFromFileTTF(filename.c_str(), size_pixels, font_cfg_template, glyph_ranges);
        return self.AddFontFromFileTTF(filename.c_str(), size_pixels);
    }
    , py::arg("filename")
    , py::arg("size_pixels")
    //, py::arg("font_cfg") = nullptr
    //, py::arg("glyph_ranges") = nullptr
    , py::return_value_policy::automatic_reference);
    FontAtlas.def("get_tex_data_as_alpha8", [](ImFontAtlas& atlas)
    {
        unsigned char* pixels;
        int width, height, bytes_per_pixel;
        atlas.GetTexDataAsAlpha8(&pixels, &width, &height, &bytes_per_pixel);
        std::string data((char*)pixels, width * height * bytes_per_pixel);
        return std::make_tuple(width, height, py::bytes(data));
    });
    FontAtlas.def("get_tex_data_as_rgba32", [](ImFontAtlas& atlas)
    {
        unsigned char* pixels;
        int width, height, bytes_per_pixel;
        atlas.GetTexDataAsRGBA32(&pixels, &width, &height, &bytes_per_pixel);
        std::string data((char*)pixels, width * height * bytes_per_pixel);
        return std::make_tuple(width, height, py::bytes(data));
    });
    PYEXTEND_END

    _aimgui.def("init", []()
    {
        ImGui::CreateContext();
        ImGuiIO& io = ImGui::GetIO();
        io.DisplaySize = ImVec2(800.0, 600.0);
        unsigned char* pixels;
        int w, h;
        io.Fonts->GetTexDataAsAlpha8(&pixels, &w, &h, nullptr);
    });

    _aimgui.def("input_text", [](const char* label, char* data, size_t max_size, ImGuiInputTextFlags flags)
    {
        max_size++;
        char* text = (char*)malloc(max_size * sizeof(char));
        strncpy(text, data, max_size);
        auto ret = ImGui::InputText(label, text, max_size, flags, nullptr, NULL);
        std::string output(text);
        free(text);
        return std::make_tuple(ret, output);
    }
    , py::arg("label")
    , py::arg("data")
    , py::arg("max_size")
    , py::arg("flags") = 0
    , py::return_value_policy::automatic_reference);
    _aimgui.def("input_text_multiline", [](const char* label, char* data, size_t max_size, const ImVec2& size, ImGuiInputTextFlags flags)
    {
        max_size++;
        char* text = (char*)malloc(max_size * sizeof(char));
        strncpy(text, data, max_size);
        auto ret = ImGui::InputTextMultiline(label, text, max_size, size, flags, nullptr, NULL);
        std::string output(text);
        free(text);
        return std::make_tuple(ret, output);
    }
    , py::arg("label")
    , py::arg("data")
    , py::arg("max_size")
    , py::arg("size") = ImVec2(0,0)
    , py::arg("flags") = 0
    , py::return_value_policy::automatic_reference);
    _aimgui.def("menu_item", [](const char * label, const char * shortcut, bool * p_selected, bool enabled)
    {
        auto ret = ImGui::MenuItem(label, shortcut, p_selected, enabled);
        return std::make_tuple(ret, p_selected);
    }
    , py::arg("label")
    , py::arg("shortcut")
    , py::arg("p_selected")
    , py::arg("enabled") = true
    , py::return_value_policy::automatic_reference);
    _aimgui.def("combo", [](const char* label, int * current_item, std::vector<std::string> items, int popup_max_height_in_items)
    {
        std::vector<const char*> ptrs;
        for (const std::string& s : items)
        {
            ptrs.push_back(s.c_str());
        }
        auto ret = ImGui::Combo(label, current_item, ptrs.data(), ptrs.size(), popup_max_height_in_items);
        return std::make_tuple(ret, current_item);
    }
    , py::arg("label")
    , py::arg("current_item")
    , py::arg("items")
    , py::arg("popup_max_height_in_items") = -1
    , py::return_value_policy::automatic_reference);

    _aimgui.def("selectable", [](const char * label, bool * p_selected, ImGuiSelectableFlags flags, const ImVec2 & size)
    {
        auto ret = ImGui::Selectable(label, p_selected, flags, size);
        return std::make_tuple(ret, p_selected);
    }
    , py::arg("label")
    , py::arg("p_selected")
    , py::arg("flags") = 0
    , py::arg("size") = ImVec2(0,0)
    , py::return_value_policy::automatic_reference);

    _aimgui.def("list_box", [](const char* label, int * current_item, std::vector<std::string> items, int height_in_items)
    {
        std::vector<const char*> ptrs;
        for (const std::string& s : items)
        {
            ptrs.push_back(s.c_str());
        }
        auto ret = ImGui::ListBox(label, current_item, ptrs.data(), ptrs.size(), height_in_items);
        return std::make_tuple(ret, current_item);
    }
    , py::arg("label")
    , py::arg("current_item")
    , py::arg("items")
    , py::arg("height_in_items") = -1
    , py::return_value_policy::automatic_reference);

    _aimgui.def("collapsing_header", [](const char * label, bool * p_open, ImGuiTreeNodeFlags flags)
    {
        auto ret = ImGui::CollapsingHeader(label, p_open, flags);
        return std::make_tuple(ret, p_open);
    }
    , py::arg("label")
    , py::arg("p_open")
    , py::arg("flags") = 0
    , py::return_value_policy::automatic_reference);

    _aimgui.def("plot_lines", [](const char* label, std::vector<float> values, int values_offset, const char* overlay_text, float scale_min, float scale_max, ImVec2 graph_size)
    {
        ImGui::PlotLines(label, values.data(), values.size(), values_offset, overlay_text, scale_min, scale_max, graph_size, sizeof(float));
    }
    , py::arg("label")
    , py::arg("values")
    , py::arg("values_offset") = 0
    , py::arg("overlay_text") = nullptr
    , py::arg("scale_min") = FLT_MAX
    , py::arg("scale_max") = FLT_MAX
    , py::arg("graph_size") = ImVec2(0,0)
    );
    _aimgui.def("plot_histogram", [](const char* label, std::vector<float> values, int values_offset, const char* overlay_text, float scale_min, float scale_max, ImVec2 graph_size)
    {
        ImGui::PlotHistogram(label, values.data(), values.size(), values_offset, overlay_text, scale_min, scale_max, graph_size, sizeof(float));
    }
    , py::arg("label")
    , py::arg("values")
    , py::arg("values_offset") = 0
    , py::arg("overlay_text") = nullptr
    , py::arg("scale_min") = FLT_MAX
    , py::arg("scale_max") = FLT_MAX
    , py::arg("graph_size") = ImVec2(0,0)
    );
}

