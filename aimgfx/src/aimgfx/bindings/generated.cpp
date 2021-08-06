
#include <limits>

#include <pybind11/pybind11.h>
#include <pybind11/functional.h>
#include <pybind11/stl.h>

#include <aimgui/bindtools.h>

#include <aimgfx/aimgfx.h>
#include <bx/allocator.h>

using namespace bgfx;

namespace py = pybind11;

void init_generated(py::module &libaimgfx, Registry &registry) {

    libaimgfx.def("is_valid", py::overload_cast<bgfx::DynamicIndexBufferHandle>(&bgfx::isValid)
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("is_valid", py::overload_cast<bgfx::DynamicVertexBufferHandle>(&bgfx::isValid)
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("is_valid", py::overload_cast<bgfx::FrameBufferHandle>(&bgfx::isValid)
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("is_valid", py::overload_cast<bgfx::IndexBufferHandle>(&bgfx::isValid)
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("is_valid", py::overload_cast<bgfx::IndirectBufferHandle>(&bgfx::isValid)
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("is_valid", py::overload_cast<bgfx::OcclusionQueryHandle>(&bgfx::isValid)
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("is_valid", py::overload_cast<bgfx::ProgramHandle>(&bgfx::isValid)
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("is_valid", py::overload_cast<bgfx::ShaderHandle>(&bgfx::isValid)
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("is_valid", py::overload_cast<bgfx::TextureHandle>(&bgfx::isValid)
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("is_valid", py::overload_cast<bgfx::UniformHandle>(&bgfx::isValid)
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("is_valid", py::overload_cast<bgfx::VertexBufferHandle>(&bgfx::isValid)
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("is_valid", py::overload_cast<bgfx::VertexLayoutHandle>(&bgfx::isValid)
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("vertex_unpack", [](std::array<float, 4>& _output, Attrib::Enum _attr, const bgfx::VertexLayout & _layout, const void * _data, uint32_t _index)
    {
        bgfx::vertexUnpack(&_output[0], _attr, _layout, _data, _index);
        return _output;
    }
    , py::arg("_output")
    , py::arg("_attr")
    , py::arg("_layout")
    , py::arg("_data")
    , py::arg("_index") = 0
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("vertex_convert", &bgfx::vertexConvert
    , py::arg("_dest_layout")
    , py::arg("_dest_data")
    , py::arg("_src_layout")
    , py::arg("_src_data")
    , py::arg("_num") = 1
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("weld_vertices", &bgfx::weldVertices
    , py::arg("_output")
    , py::arg("_layout")
    , py::arg("_data")
    , py::arg("_num")
    , py::arg("_index32")
    , py::arg("_epsilon") = 0.001f
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("topology_convert", &bgfx::topologyConvert
    , py::arg("_conversion")
    , py::arg("_dst")
    , py::arg("_dst_size")
    , py::arg("_indices")
    , py::arg("_num_indices")
    , py::arg("_index32")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("get_supported_renderers", &bgfx::getSupportedRenderers
    , py::arg("_max") = 0
    , py::arg("_enum") = nullptr
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("get_renderer_name", &bgfx::getRendererName
    , py::arg("_type")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("init", &bgfx::init
    , py::arg("_init") = bgfx::Init()
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("shutdown", &bgfx::shutdown
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("reset", &bgfx::reset
    , py::arg("_width")
    , py::arg("_height")
    , py::arg("_flags") = BGFX_RESET_NONE
    , py::arg("_format") = TextureFormat::Count
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("begin", &bgfx::begin
    , py::arg("_for_thread") = false
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("end", &bgfx::end
    , py::arg("_encoder")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("frame", &bgfx::frame
    , py::arg("_capture") = false
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("get_renderer_type", &bgfx::getRendererType
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("get_caps", &bgfx::getCaps
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("get_stats", &bgfx::getStats
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("alloc", &bgfx::alloc
    , py::arg("_size")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("copy", &bgfx::copy
    , py::arg("_data")
    , py::arg("_size")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_debug", &bgfx::setDebug
    , py::arg("_debug")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("dbg_text_clear", &bgfx::dbgTextClear
    , py::arg("_attr") = 0
    , py::arg("_small") = false
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("dbg_text_printf", [](uint16_t _x, uint16_t _y, uint8_t _attr, const char * _format)
    {
        bgfx::dbgTextPrintf(_x, _y, _attr, _format);
        return ;
    }
    , py::arg("_x")
    , py::arg("_y")
    , py::arg("_attr")
    , py::arg("_format")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("dbg_text_image", &bgfx::dbgTextImage
    , py::arg("_x")
    , py::arg("_y")
    , py::arg("_width")
    , py::arg("_height")
    , py::arg("_data")
    , py::arg("_pitch")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("create_index_buffer", &bgfx::createIndexBuffer
    , py::arg("_mem")
    , py::arg("_flags") = BGFX_BUFFER_NONE
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_name", py::overload_cast<bgfx::IndexBufferHandle, const char *, int32_t>(&bgfx::setName)
    , py::arg("_handle")
    , py::arg("_name")
    , py::arg("_len") = INT32_MAX
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("destroy", py::overload_cast<bgfx::IndexBufferHandle>(&bgfx::destroy)
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("create_vertex_layout", &bgfx::createVertexLayout
    , py::arg("_layout")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("destroy", py::overload_cast<bgfx::VertexLayoutHandle>(&bgfx::destroy)
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("create_vertex_buffer", &bgfx::createVertexBuffer
    , py::arg("_mem")
    , py::arg("_layout")
    , py::arg("_flags") = BGFX_BUFFER_NONE
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_name", py::overload_cast<bgfx::VertexBufferHandle, const char *, int32_t>(&bgfx::setName)
    , py::arg("_handle")
    , py::arg("_name")
    , py::arg("_len") = INT32_MAX
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("destroy", py::overload_cast<bgfx::VertexBufferHandle>(&bgfx::destroy)
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("create_dynamic_index_buffer", py::overload_cast<uint32_t, uint16_t>(&bgfx::createDynamicIndexBuffer)
    , py::arg("_num")
    , py::arg("_flags") = BGFX_BUFFER_NONE
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("create_dynamic_index_buffer", py::overload_cast<const bgfx::Memory *, uint16_t>(&bgfx::createDynamicIndexBuffer)
    , py::arg("_mem")
    , py::arg("_flags") = BGFX_BUFFER_NONE
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("update", py::overload_cast<bgfx::DynamicIndexBufferHandle, uint32_t, const bgfx::Memory *>(&bgfx::update)
    , py::arg("_handle")
    , py::arg("_start_index")
    , py::arg("_mem")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("destroy", py::overload_cast<bgfx::DynamicIndexBufferHandle>(&bgfx::destroy)
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("create_dynamic_vertex_buffer", py::overload_cast<uint32_t, const bgfx::VertexLayout &, uint16_t>(&bgfx::createDynamicVertexBuffer)
    , py::arg("_num")
    , py::arg("_layout")
    , py::arg("_flags") = BGFX_BUFFER_NONE
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("create_dynamic_vertex_buffer", py::overload_cast<const bgfx::Memory *, const bgfx::VertexLayout &, uint16_t>(&bgfx::createDynamicVertexBuffer)
    , py::arg("_mem")
    , py::arg("_layout")
    , py::arg("_flags") = BGFX_BUFFER_NONE
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("update", py::overload_cast<bgfx::DynamicVertexBufferHandle, uint32_t, const bgfx::Memory *>(&bgfx::update)
    , py::arg("_handle")
    , py::arg("_start_vertex")
    , py::arg("_mem")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("destroy", py::overload_cast<bgfx::DynamicVertexBufferHandle>(&bgfx::destroy)
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("get_avail_transient_index_buffer", &bgfx::getAvailTransientIndexBuffer
    , py::arg("_num")
    , py::arg("_index32") = false
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("get_avail_transient_vertex_buffer", &bgfx::getAvailTransientVertexBuffer
    , py::arg("_num")
    , py::arg("_layout")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("get_avail_instance_data_buffer", &bgfx::getAvailInstanceDataBuffer
    , py::arg("_num")
    , py::arg("_stride")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("alloc_transient_index_buffer", &bgfx::allocTransientIndexBuffer
    , py::arg("_tib")
    , py::arg("_num")
    , py::arg("_index32") = false
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("alloc_transient_vertex_buffer", &bgfx::allocTransientVertexBuffer
    , py::arg("_tvb")
    , py::arg("_num")
    , py::arg("_layout")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("alloc_transient_buffers", &bgfx::allocTransientBuffers
    , py::arg("_tvb")
    , py::arg("_layout")
    , py::arg("_num_vertices")
    , py::arg("_tib")
    , py::arg("_num_indices")
    , py::arg("_index32") = false
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("alloc_instance_data_buffer", &bgfx::allocInstanceDataBuffer
    , py::arg("_idb")
    , py::arg("_num")
    , py::arg("_stride")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("create_indirect_buffer", &bgfx::createIndirectBuffer
    , py::arg("_num")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("destroy", py::overload_cast<bgfx::IndirectBufferHandle>(&bgfx::destroy)
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("create_shader", &bgfx::createShader
    , py::arg("_mem")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("get_shader_uniforms", &bgfx::getShaderUniforms
    , py::arg("_handle")
    , py::arg("_uniforms") = nullptr
    , py::arg("_max") = 0
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_name", py::overload_cast<bgfx::ShaderHandle, const char *, int32_t>(&bgfx::setName)
    , py::arg("_handle")
    , py::arg("_name")
    , py::arg("_len") = INT32_MAX
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("destroy", py::overload_cast<bgfx::ShaderHandle>(&bgfx::destroy)
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("create_program", py::overload_cast<bgfx::ShaderHandle, bgfx::ShaderHandle, bool>(&bgfx::createProgram)
    , py::arg("_vsh")
    , py::arg("_fsh")
    , py::arg("_destroy_shaders") = false
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("create_program", py::overload_cast<bgfx::ShaderHandle, bool>(&bgfx::createProgram)
    , py::arg("_csh")
    , py::arg("_destroy_shader") = false
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("destroy", py::overload_cast<bgfx::ProgramHandle>(&bgfx::destroy)
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("is_texture_valid", &bgfx::isTextureValid
    , py::arg("_depth")
    , py::arg("_cube_map")
    , py::arg("_num_layers")
    , py::arg("_format")
    , py::arg("_flags")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("is_frame_buffer_valid", &bgfx::isFrameBufferValid
    , py::arg("_num")
    , py::arg("_attachment")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("calc_texture_size", [](bgfx::TextureInfo & _info, uint16_t _width, uint16_t _height, uint16_t _depth, bool _cubeMap, bool _hasMips, uint16_t _numLayers, TextureFormat::Enum _format)
    {
        bgfx::calcTextureSize(_info, _width, _height, _depth, _cubeMap, _hasMips, _numLayers, _format);
        return _info;
    }
    , py::arg("_info")
    , py::arg("_width")
    , py::arg("_height")
    , py::arg("_depth")
    , py::arg("_cube_map")
    , py::arg("_has_mips")
    , py::arg("_num_layers")
    , py::arg("_format")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("create_texture", &bgfx::createTexture
    , py::arg("_mem")
    , py::arg("_flags") = BGFX_TEXTURE_NONE|BGFX_SAMPLER_NONE
    , py::arg("_skip") = 0
    , py::arg("_info") = nullptr
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("create_texture2_d", py::overload_cast<uint16_t, uint16_t, bool, uint16_t, TextureFormat::Enum, uint64_t, const bgfx::Memory *>(&bgfx::createTexture2D)
    , py::arg("_width")
    , py::arg("_height")
    , py::arg("_has_mips")
    , py::arg("_num_layers")
    , py::arg("_format")
    , py::arg("_flags") = BGFX_TEXTURE_NONE|BGFX_SAMPLER_NONE
    , py::arg("_mem") = nullptr
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("create_texture2_d", py::overload_cast<BackbufferRatio::Enum, bool, uint16_t, TextureFormat::Enum, uint64_t>(&bgfx::createTexture2D)
    , py::arg("_ratio")
    , py::arg("_has_mips")
    , py::arg("_num_layers")
    , py::arg("_format")
    , py::arg("_flags") = BGFX_TEXTURE_NONE|BGFX_SAMPLER_NONE
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("create_texture3_d", &bgfx::createTexture3D
    , py::arg("_width")
    , py::arg("_height")
    , py::arg("_depth")
    , py::arg("_has_mips")
    , py::arg("_format")
    , py::arg("_flags") = BGFX_TEXTURE_NONE|BGFX_SAMPLER_NONE
    , py::arg("_mem") = nullptr
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("create_texture_cube", &bgfx::createTextureCube
    , py::arg("_size")
    , py::arg("_has_mips")
    , py::arg("_num_layers")
    , py::arg("_format")
    , py::arg("_flags") = BGFX_TEXTURE_NONE|BGFX_SAMPLER_NONE
    , py::arg("_mem") = nullptr
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("update_texture2_d", &bgfx::updateTexture2D
    , py::arg("_handle")
    , py::arg("_layer")
    , py::arg("_mip")
    , py::arg("_x")
    , py::arg("_y")
    , py::arg("_width")
    , py::arg("_height")
    , py::arg("_mem")
    , py::arg("_pitch") = UINT16_MAX
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("update_texture3_d", &bgfx::updateTexture3D
    , py::arg("_handle")
    , py::arg("_mip")
    , py::arg("_x")
    , py::arg("_y")
    , py::arg("_z")
    , py::arg("_width")
    , py::arg("_height")
    , py::arg("_depth")
    , py::arg("_mem")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("update_texture_cube", &bgfx::updateTextureCube
    , py::arg("_handle")
    , py::arg("_layer")
    , py::arg("_side")
    , py::arg("_mip")
    , py::arg("_x")
    , py::arg("_y")
    , py::arg("_width")
    , py::arg("_height")
    , py::arg("_mem")
    , py::arg("_pitch") = UINT16_MAX
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("read_texture", &bgfx::readTexture
    , py::arg("_handle")
    , py::arg("_data")
    , py::arg("_mip") = 0
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_name", py::overload_cast<bgfx::TextureHandle, const char *, int32_t>(&bgfx::setName)
    , py::arg("_handle")
    , py::arg("_name")
    , py::arg("_len") = INT32_MAX
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("get_direct_access_ptr", &bgfx::getDirectAccessPtr
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("destroy", py::overload_cast<bgfx::TextureHandle>(&bgfx::destroy)
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("create_frame_buffer", py::overload_cast<uint16_t, uint16_t, TextureFormat::Enum, uint64_t>(&bgfx::createFrameBuffer)
    , py::arg("_width")
    , py::arg("_height")
    , py::arg("_format")
    , py::arg("_texture_flags") = BGFX_SAMPLER_U_CLAMP|BGFX_SAMPLER_V_CLAMP
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("create_frame_buffer", py::overload_cast<BackbufferRatio::Enum, TextureFormat::Enum, uint64_t>(&bgfx::createFrameBuffer)
    , py::arg("_ratio")
    , py::arg("_format")
    , py::arg("_texture_flags") = BGFX_SAMPLER_U_CLAMP|BGFX_SAMPLER_V_CLAMP
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("create_frame_buffer", py::overload_cast<uint8_t, const bgfx::TextureHandle *, bool>(&bgfx::createFrameBuffer)
    , py::arg("_num")
    , py::arg("_handles")
    , py::arg("_destroy_textures") = false
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("create_frame_buffer", py::overload_cast<uint8_t, const bgfx::Attachment *, bool>(&bgfx::createFrameBuffer)
    , py::arg("_num")
    , py::arg("_attachment")
    , py::arg("_destroy_textures") = false
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("create_frame_buffer", py::overload_cast<void *, uint16_t, uint16_t, TextureFormat::Enum, TextureFormat::Enum>(&bgfx::createFrameBuffer)
    , py::arg("_nwh")
    , py::arg("_width")
    , py::arg("_height")
    , py::arg("_format") = TextureFormat::Count
    , py::arg("_depth_format") = TextureFormat::Count
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_name", py::overload_cast<bgfx::FrameBufferHandle, const char *, int32_t>(&bgfx::setName)
    , py::arg("_handle")
    , py::arg("_name")
    , py::arg("_len") = INT32_MAX
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("get_texture", &bgfx::getTexture
    , py::arg("_handle")
    , py::arg("_attachment") = 0
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("destroy", py::overload_cast<bgfx::FrameBufferHandle>(&bgfx::destroy)
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("create_uniform", &bgfx::createUniform
    , py::arg("_name")
    , py::arg("_type")
    , py::arg("_num") = 1
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("get_uniform_info", [](bgfx::UniformHandle _handle, bgfx::UniformInfo & _info)
    {
        bgfx::getUniformInfo(_handle, _info);
        return _info;
    }
    , py::arg("_handle")
    , py::arg("_info")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("destroy", py::overload_cast<bgfx::UniformHandle>(&bgfx::destroy)
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("create_occlusion_query", &bgfx::createOcclusionQuery
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("get_result", [](bgfx::OcclusionQueryHandle _handle, int32_t * _result)
    {
        auto ret = bgfx::getResult(_handle, _result);
        return std::make_tuple(ret, _result);
    }
    , py::arg("_handle")
    , py::arg("_result") = nullptr
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("destroy", py::overload_cast<bgfx::OcclusionQueryHandle>(&bgfx::destroy)
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_view_name", &bgfx::setViewName
    , py::arg("_id")
    , py::arg("_name")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_view_rect", py::overload_cast<bgfx::ViewId, uint16_t, uint16_t, uint16_t, uint16_t>(&bgfx::setViewRect)
    , py::arg("_id")
    , py::arg("_x")
    , py::arg("_y")
    , py::arg("_width")
    , py::arg("_height")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_view_rect", py::overload_cast<bgfx::ViewId, uint16_t, uint16_t, BackbufferRatio::Enum>(&bgfx::setViewRect)
    , py::arg("_id")
    , py::arg("_x")
    , py::arg("_y")
    , py::arg("_ratio")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_view_scissor", &bgfx::setViewScissor
    , py::arg("_id")
    , py::arg("_x") = 0
    , py::arg("_y") = 0
    , py::arg("_width") = 0
    , py::arg("_height") = 0
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_view_clear", py::overload_cast<bgfx::ViewId, uint16_t, uint32_t, float, uint8_t>(&bgfx::setViewClear)
    , py::arg("_id")
    , py::arg("_flags")
    , py::arg("_rgba") = 0x000000ff
    , py::arg("_depth") = 1.0f
    , py::arg("_stencil") = 0
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_view_clear", py::overload_cast<bgfx::ViewId, uint16_t, float, uint8_t, uint8_t, uint8_t, uint8_t, uint8_t, uint8_t, uint8_t, uint8_t, uint8_t>(&bgfx::setViewClear)
    , py::arg("_id")
    , py::arg("_flags")
    , py::arg("_depth")
    , py::arg("_stencil")
    , py::arg("_0") = UINT8_MAX
    , py::arg("_1") = UINT8_MAX
    , py::arg("_2") = UINT8_MAX
    , py::arg("_3") = UINT8_MAX
    , py::arg("_4") = UINT8_MAX
    , py::arg("_5") = UINT8_MAX
    , py::arg("_6") = UINT8_MAX
    , py::arg("_7") = UINT8_MAX
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_view_mode", &bgfx::setViewMode
    , py::arg("_id")
    , py::arg("_mode") = ViewMode::Default
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_view_frame_buffer", &bgfx::setViewFrameBuffer
    , py::arg("_id")
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_view_transform", &bgfx::setViewTransform
    , py::arg("_id")
    , py::arg("_view")
    , py::arg("_proj")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_view_order", &bgfx::setViewOrder
    , py::arg("_id") = 0
    , py::arg("_num") = UINT16_MAX
    , py::arg("_remap") = nullptr
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("reset_view", &bgfx::resetView
    , py::arg("_id")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_marker", &bgfx::setMarker
    , py::arg("_marker")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_state", &bgfx::setState
    , py::arg("_state")
    , py::arg("_rgba") = 0
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_condition", &bgfx::setCondition
    , py::arg("_handle")
    , py::arg("_visible")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_stencil", &bgfx::setStencil
    , py::arg("_fstencil")
    , py::arg("_bstencil") = BGFX_STENCIL_NONE
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_scissor", py::overload_cast<uint16_t, uint16_t, uint16_t, uint16_t>(&bgfx::setScissor)
    , py::arg("_x")
    , py::arg("_y")
    , py::arg("_width")
    , py::arg("_height")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_scissor", py::overload_cast<uint16_t>(&bgfx::setScissor)
    , py::arg("_cache") = UINT16_MAX
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_transform", py::overload_cast<const void *, uint16_t>(&bgfx::setTransform)
    , py::arg("_mtx")
    , py::arg("_num") = 1
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("alloc_transform", &bgfx::allocTransform
    , py::arg("_transform")
    , py::arg("_num")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_transform", py::overload_cast<uint32_t, uint16_t>(&bgfx::setTransform)
    , py::arg("_cache")
    , py::arg("_num") = 1
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_uniform", &bgfx::setUniform
    , py::arg("_handle")
    , py::arg("_value")
    , py::arg("_num") = 1
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_index_buffer", py::overload_cast<bgfx::IndexBufferHandle>(&bgfx::setIndexBuffer)
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_index_buffer", py::overload_cast<bgfx::IndexBufferHandle, uint32_t, uint32_t>(&bgfx::setIndexBuffer)
    , py::arg("_handle")
    , py::arg("_first_index")
    , py::arg("_num_indices")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_index_buffer", py::overload_cast<bgfx::DynamicIndexBufferHandle>(&bgfx::setIndexBuffer)
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_index_buffer", py::overload_cast<bgfx::DynamicIndexBufferHandle, uint32_t, uint32_t>(&bgfx::setIndexBuffer)
    , py::arg("_handle")
    , py::arg("_first_index")
    , py::arg("_num_indices")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_index_buffer", py::overload_cast<const bgfx::TransientIndexBuffer *>(&bgfx::setIndexBuffer)
    , py::arg("_tib")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_index_buffer", py::overload_cast<const bgfx::TransientIndexBuffer *, uint32_t, uint32_t>(&bgfx::setIndexBuffer)
    , py::arg("_tib")
    , py::arg("_first_index")
    , py::arg("_num_indices")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_vertex_buffer", py::overload_cast<uint8_t, bgfx::VertexBufferHandle>(&bgfx::setVertexBuffer)
    , py::arg("_stream")
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_vertex_buffer", py::overload_cast<uint8_t, bgfx::VertexBufferHandle, uint32_t, uint32_t, bgfx::VertexLayoutHandle>(&bgfx::setVertexBuffer)
    , py::arg("_stream")
    , py::arg("_handle")
    , py::arg("_start_vertex")
    , py::arg("_num_vertices")
    , py::arg("_layout_handle") = bgfx::VertexLayoutHandle(BGFX_INVALID_HANDLE)
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_vertex_buffer", py::overload_cast<uint8_t, bgfx::DynamicVertexBufferHandle>(&bgfx::setVertexBuffer)
    , py::arg("_stream")
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_vertex_buffer", py::overload_cast<uint8_t, bgfx::DynamicVertexBufferHandle, uint32_t, uint32_t, bgfx::VertexLayoutHandle>(&bgfx::setVertexBuffer)
    , py::arg("_stream")
    , py::arg("_handle")
    , py::arg("_start_vertex")
    , py::arg("_num_vertices")
    , py::arg("_layout_handle") = bgfx::VertexLayoutHandle(BGFX_INVALID_HANDLE)
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_vertex_buffer", py::overload_cast<uint8_t, const bgfx::TransientVertexBuffer *>(&bgfx::setVertexBuffer)
    , py::arg("_stream")
    , py::arg("_tvb")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_vertex_buffer", py::overload_cast<uint8_t, const bgfx::TransientVertexBuffer *, uint32_t, uint32_t, bgfx::VertexLayoutHandle>(&bgfx::setVertexBuffer)
    , py::arg("_stream")
    , py::arg("_tvb")
    , py::arg("_start_vertex")
    , py::arg("_num_vertices")
    , py::arg("_layout_handle") = bgfx::VertexLayoutHandle(BGFX_INVALID_HANDLE)
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_vertex_count", &bgfx::setVertexCount
    , py::arg("_num_vertices")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_instance_data_buffer", py::overload_cast<const bgfx::InstanceDataBuffer *>(&bgfx::setInstanceDataBuffer)
    , py::arg("_idb")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_instance_data_buffer", py::overload_cast<const bgfx::InstanceDataBuffer *, uint32_t, uint32_t>(&bgfx::setInstanceDataBuffer)
    , py::arg("_idb")
    , py::arg("_start")
    , py::arg("_num")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_instance_data_buffer", py::overload_cast<bgfx::VertexBufferHandle, uint32_t, uint32_t>(&bgfx::setInstanceDataBuffer)
    , py::arg("_handle")
    , py::arg("_start")
    , py::arg("_num")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_instance_data_buffer", py::overload_cast<bgfx::DynamicVertexBufferHandle, uint32_t, uint32_t>(&bgfx::setInstanceDataBuffer)
    , py::arg("_handle")
    , py::arg("_start")
    , py::arg("_num")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_instance_count", &bgfx::setInstanceCount
    , py::arg("_num_instances")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_texture", &bgfx::setTexture
    , py::arg("_stage")
    , py::arg("_sampler")
    , py::arg("_handle")
    , py::arg("_flags") = UINT32_MAX
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("touch", &bgfx::touch
    , py::arg("_id")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("submit", py::overload_cast<bgfx::ViewId, bgfx::ProgramHandle, uint32_t, uint8_t>(&bgfx::submit)
    , py::arg("_id")
    , py::arg("_program")
    , py::arg("_depth") = 0
    , py::arg("_flags") = BGFX_DISCARD_ALL
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("submit", py::overload_cast<bgfx::ViewId, bgfx::ProgramHandle, bgfx::OcclusionQueryHandle, uint32_t, uint8_t>(&bgfx::submit)
    , py::arg("_id")
    , py::arg("_program")
    , py::arg("_occlusion_query")
    , py::arg("_depth") = 0
    , py::arg("_flags") = BGFX_DISCARD_ALL
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("submit", py::overload_cast<bgfx::ViewId, bgfx::ProgramHandle, bgfx::IndirectBufferHandle, uint16_t, uint16_t, uint32_t, uint8_t>(&bgfx::submit)
    , py::arg("_id")
    , py::arg("_program")
    , py::arg("_indirect_handle")
    , py::arg("_start") = 0
    , py::arg("_num") = 1
    , py::arg("_depth") = 0
    , py::arg("_flags") = BGFX_DISCARD_ALL
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_buffer", py::overload_cast<uint8_t, bgfx::IndexBufferHandle, Access::Enum>(&bgfx::setBuffer)
    , py::arg("_stage")
    , py::arg("_handle")
    , py::arg("_access")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_buffer", py::overload_cast<uint8_t, bgfx::VertexBufferHandle, Access::Enum>(&bgfx::setBuffer)
    , py::arg("_stage")
    , py::arg("_handle")
    , py::arg("_access")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_buffer", py::overload_cast<uint8_t, bgfx::DynamicIndexBufferHandle, Access::Enum>(&bgfx::setBuffer)
    , py::arg("_stage")
    , py::arg("_handle")
    , py::arg("_access")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_buffer", py::overload_cast<uint8_t, bgfx::DynamicVertexBufferHandle, Access::Enum>(&bgfx::setBuffer)
    , py::arg("_stage")
    , py::arg("_handle")
    , py::arg("_access")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_buffer", py::overload_cast<uint8_t, bgfx::IndirectBufferHandle, Access::Enum>(&bgfx::setBuffer)
    , py::arg("_stage")
    , py::arg("_handle")
    , py::arg("_access")
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("set_image", &bgfx::setImage
    , py::arg("_stage")
    , py::arg("_handle")
    , py::arg("_mip")
    , py::arg("_access")
    , py::arg("_format") = TextureFormat::Count
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("dispatch", py::overload_cast<bgfx::ViewId, bgfx::ProgramHandle, uint32_t, uint32_t, uint32_t, uint8_t>(&bgfx::dispatch)
    , py::arg("_id")
    , py::arg("_handle")
    , py::arg("_num_x") = 1
    , py::arg("_num_y") = 1
    , py::arg("_num_z") = 1
    , py::arg("_flags") = BGFX_DISCARD_ALL
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("dispatch", py::overload_cast<bgfx::ViewId, bgfx::ProgramHandle, bgfx::IndirectBufferHandle, uint16_t, uint16_t, uint8_t>(&bgfx::dispatch)
    , py::arg("_id")
    , py::arg("_handle")
    , py::arg("_indirect_handle")
    , py::arg("_start") = 0
    , py::arg("_num") = 1
    , py::arg("_flags") = BGFX_DISCARD_ALL
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("discard", &bgfx::discard
    , py::arg("_flags") = BGFX_DISCARD_ALL
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("blit", py::overload_cast<bgfx::ViewId, bgfx::TextureHandle, uint16_t, uint16_t, bgfx::TextureHandle, uint16_t, uint16_t, uint16_t, uint16_t>(&bgfx::blit)
    , py::arg("_id")
    , py::arg("_dst")
    , py::arg("_dst_x")
    , py::arg("_dst_y")
    , py::arg("_src")
    , py::arg("_src_x") = 0
    , py::arg("_src_y") = 0
    , py::arg("_width") = UINT16_MAX
    , py::arg("_height") = UINT16_MAX
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("blit", py::overload_cast<bgfx::ViewId, bgfx::TextureHandle, uint8_t, uint16_t, uint16_t, uint16_t, bgfx::TextureHandle, uint8_t, uint16_t, uint16_t, uint16_t, uint16_t, uint16_t, uint16_t>(&bgfx::blit)
    , py::arg("_id")
    , py::arg("_dst")
    , py::arg("_dst_mip")
    , py::arg("_dst_x")
    , py::arg("_dst_y")
    , py::arg("_dst_z")
    , py::arg("_src")
    , py::arg("_src_mip") = 0
    , py::arg("_src_x") = 0
    , py::arg("_src_y") = 0
    , py::arg("_src_z") = 0
    , py::arg("_width") = UINT16_MAX
    , py::arg("_height") = UINT16_MAX
    , py::arg("_depth") = UINT16_MAX
    , py::return_value_policy::automatic_reference);
    libaimgfx.def("request_screen_shot", &bgfx::requestScreenShot
    , py::arg("_handle")
    , py::arg("_file_path")
    , py::return_value_policy::automatic_reference);

        PYCLASS_BEGIN(libaimgfx, bgfx::Fatal, Fatal)
    PYCLASS_END(libaimgfx, bgfx::Fatal, Fatal)


        PYCLASS_BEGIN(libaimgfx, bgfx::RendererType, RendererType)
    PYCLASS_END(libaimgfx, bgfx::RendererType, RendererType)


        PYCLASS_BEGIN(libaimgfx, bgfx::Access, Access)
    PYCLASS_END(libaimgfx, bgfx::Access, Access)


        PYCLASS_BEGIN(libaimgfx, bgfx::Attrib, Attrib)
    PYCLASS_END(libaimgfx, bgfx::Attrib, Attrib)


        PYCLASS_BEGIN(libaimgfx, bgfx::AttribType, AttribType)
    PYCLASS_END(libaimgfx, bgfx::AttribType, AttribType)


        PYCLASS_BEGIN(libaimgfx, bgfx::TextureFormat, TextureFormat)
    PYCLASS_END(libaimgfx, bgfx::TextureFormat, TextureFormat)


        PYCLASS_BEGIN(libaimgfx, bgfx::UniformType, UniformType)
    PYCLASS_END(libaimgfx, bgfx::UniformType, UniformType)


        PYCLASS_BEGIN(libaimgfx, bgfx::BackbufferRatio, BackbufferRatio)
    PYCLASS_END(libaimgfx, bgfx::BackbufferRatio, BackbufferRatio)


        PYCLASS_BEGIN(libaimgfx, bgfx::OcclusionQueryResult, OcclusionQueryResult)
    PYCLASS_END(libaimgfx, bgfx::OcclusionQueryResult, OcclusionQueryResult)


        PYCLASS_BEGIN(libaimgfx, bgfx::Topology, Topology)
    PYCLASS_END(libaimgfx, bgfx::Topology, Topology)


        PYCLASS_BEGIN(libaimgfx, bgfx::TopologyConvert, TopologyConvert)
    PYCLASS_END(libaimgfx, bgfx::TopologyConvert, TopologyConvert)


        PYCLASS_BEGIN(libaimgfx, bgfx::TopologySort, TopologySort)
    PYCLASS_END(libaimgfx, bgfx::TopologySort, TopologySort)


        PYCLASS_BEGIN(libaimgfx, bgfx::ViewMode, ViewMode)
    PYCLASS_END(libaimgfx, bgfx::ViewMode, ViewMode)


        PYCLASS_BEGIN(libaimgfx, bgfx::DynamicIndexBufferHandle, DynamicIndexBufferHandle)
    DynamicIndexBufferHandle.def_readwrite("idx", &bgfx::DynamicIndexBufferHandle::idx);
    PYCLASS_END(libaimgfx, bgfx::DynamicIndexBufferHandle, DynamicIndexBufferHandle)


        PYCLASS_BEGIN(libaimgfx, bgfx::DynamicVertexBufferHandle, DynamicVertexBufferHandle)
    DynamicVertexBufferHandle.def_readwrite("idx", &bgfx::DynamicVertexBufferHandle::idx);
    PYCLASS_END(libaimgfx, bgfx::DynamicVertexBufferHandle, DynamicVertexBufferHandle)


        PYCLASS_BEGIN(libaimgfx, bgfx::FrameBufferHandle, FrameBufferHandle)
    FrameBufferHandle.def_readwrite("idx", &bgfx::FrameBufferHandle::idx);
    PYCLASS_END(libaimgfx, bgfx::FrameBufferHandle, FrameBufferHandle)


        PYCLASS_BEGIN(libaimgfx, bgfx::IndexBufferHandle, IndexBufferHandle)
    IndexBufferHandle.def_readwrite("idx", &bgfx::IndexBufferHandle::idx);
    PYCLASS_END(libaimgfx, bgfx::IndexBufferHandle, IndexBufferHandle)


        PYCLASS_BEGIN(libaimgfx, bgfx::IndirectBufferHandle, IndirectBufferHandle)
    IndirectBufferHandle.def_readwrite("idx", &bgfx::IndirectBufferHandle::idx);
    PYCLASS_END(libaimgfx, bgfx::IndirectBufferHandle, IndirectBufferHandle)


        PYCLASS_BEGIN(libaimgfx, bgfx::OcclusionQueryHandle, OcclusionQueryHandle)
    OcclusionQueryHandle.def_readwrite("idx", &bgfx::OcclusionQueryHandle::idx);
    PYCLASS_END(libaimgfx, bgfx::OcclusionQueryHandle, OcclusionQueryHandle)


        PYCLASS_BEGIN(libaimgfx, bgfx::ProgramHandle, ProgramHandle)
    ProgramHandle.def_readwrite("idx", &bgfx::ProgramHandle::idx);
    PYCLASS_END(libaimgfx, bgfx::ProgramHandle, ProgramHandle)


        PYCLASS_BEGIN(libaimgfx, bgfx::ShaderHandle, ShaderHandle)
    ShaderHandle.def_readwrite("idx", &bgfx::ShaderHandle::idx);
    PYCLASS_END(libaimgfx, bgfx::ShaderHandle, ShaderHandle)


        PYCLASS_BEGIN(libaimgfx, bgfx::TextureHandle, TextureHandle)
    TextureHandle.def_readwrite("idx", &bgfx::TextureHandle::idx);
    PYCLASS_END(libaimgfx, bgfx::TextureHandle, TextureHandle)


        PYCLASS_BEGIN(libaimgfx, bgfx::UniformHandle, UniformHandle)
    UniformHandle.def_readwrite("idx", &bgfx::UniformHandle::idx);
    PYCLASS_END(libaimgfx, bgfx::UniformHandle, UniformHandle)


        PYCLASS_BEGIN(libaimgfx, bgfx::VertexBufferHandle, VertexBufferHandle)
    VertexBufferHandle.def_readwrite("idx", &bgfx::VertexBufferHandle::idx);
    PYCLASS_END(libaimgfx, bgfx::VertexBufferHandle, VertexBufferHandle)


        PYCLASS_BEGIN(libaimgfx, bgfx::VertexLayoutHandle, VertexLayoutHandle)
    VertexLayoutHandle.def_readwrite("idx", &bgfx::VertexLayoutHandle::idx);
    PYCLASS_END(libaimgfx, bgfx::VertexLayoutHandle, VertexLayoutHandle)


        PYCLASS_BEGIN(libaimgfx, bgfx::CallbackI, CallbackI)
    CallbackI.def("fatal", &bgfx::CallbackI::fatal
    , py::arg("_file_path")
    , py::arg("_line")
    , py::arg("_code")
    , py::arg("_str")
    , py::return_value_policy::automatic_reference);
    CallbackI.def("profiler_begin", &bgfx::CallbackI::profilerBegin
    , py::arg("_name")
    , py::arg("_abgr")
    , py::arg("_file_path")
    , py::arg("_line")
    , py::return_value_policy::automatic_reference);
    CallbackI.def("profiler_begin_literal", &bgfx::CallbackI::profilerBeginLiteral
    , py::arg("_name")
    , py::arg("_abgr")
    , py::arg("_file_path")
    , py::arg("_line")
    , py::return_value_policy::automatic_reference);
    CallbackI.def("profiler_end", &bgfx::CallbackI::profilerEnd
    , py::return_value_policy::automatic_reference);
    CallbackI.def("cache_read_size", &bgfx::CallbackI::cacheReadSize
    , py::arg("_id")
    , py::return_value_policy::automatic_reference);
    CallbackI.def("cache_read", &bgfx::CallbackI::cacheRead
    , py::arg("_id")
    , py::arg("_data")
    , py::arg("_size")
    , py::return_value_policy::automatic_reference);
    CallbackI.def("cache_write", &bgfx::CallbackI::cacheWrite
    , py::arg("_id")
    , py::arg("_data")
    , py::arg("_size")
    , py::return_value_policy::automatic_reference);
    CallbackI.def("screen_shot", &bgfx::CallbackI::screenShot
    , py::arg("_file_path")
    , py::arg("_width")
    , py::arg("_height")
    , py::arg("_pitch")
    , py::arg("_data")
    , py::arg("_size")
    , py::arg("_yflip")
    , py::return_value_policy::automatic_reference);
    CallbackI.def("capture_begin", &bgfx::CallbackI::captureBegin
    , py::arg("_width")
    , py::arg("_height")
    , py::arg("_pitch")
    , py::arg("_format")
    , py::arg("_yflip")
    , py::return_value_policy::automatic_reference);
    CallbackI.def("capture_end", &bgfx::CallbackI::captureEnd
    , py::return_value_policy::automatic_reference);
    CallbackI.def("capture_frame", &bgfx::CallbackI::captureFrame
    , py::arg("_data")
    , py::arg("_size")
    , py::return_value_policy::automatic_reference);
    PYCLASS_END(libaimgfx, bgfx::CallbackI, CallbackI)


        PYCLASS_BEGIN(libaimgfx, bgfx::PlatformData, PlatformData)
    PlatformData.def(py::init<>());
    PlatformData.def_readwrite("ndt", &bgfx::PlatformData::ndt);
    PlatformData.def_readwrite("nwh", &bgfx::PlatformData::nwh);
    PlatformData.def_readwrite("context", &bgfx::PlatformData::context);
    PlatformData.def_readwrite("back_buffer", &bgfx::PlatformData::backBuffer);
    PlatformData.def_readwrite("back_buffer_ds", &bgfx::PlatformData::backBufferDS);
    PYCLASS_END(libaimgfx, bgfx::PlatformData, PlatformData)


        PYCLASS_BEGIN(libaimgfx, bgfx::Resolution, Resolution)
    Resolution.def(py::init<>());
    Resolution.def_readwrite("format", &bgfx::Resolution::format);
    Resolution.def_readwrite("width", &bgfx::Resolution::width);
    Resolution.def_readwrite("height", &bgfx::Resolution::height);
    Resolution.def_readwrite("reset", &bgfx::Resolution::reset);
    Resolution.def_readwrite("num_back_buffers", &bgfx::Resolution::numBackBuffers);
    Resolution.def_readwrite("max_frame_latency", &bgfx::Resolution::maxFrameLatency);
    PYCLASS_END(libaimgfx, bgfx::Resolution, Resolution)


        PYCLASS_BEGIN(libaimgfx, bgfx::Init, Init)
    Init.def(py::init<>());
    Init.def_readwrite("type", &bgfx::Init::type);
    Init.def_readwrite("vendor_id", &bgfx::Init::vendorId);
    Init.def_readwrite("device_id", &bgfx::Init::deviceId);
    Init.def_readwrite("capabilities", &bgfx::Init::capabilities);
    Init.def_readwrite("debug", &bgfx::Init::debug);
    Init.def_readwrite("profile", &bgfx::Init::profile);
    Init.def_readwrite("platform_data", &bgfx::Init::platformData);
    Init.def_readwrite("resolution", &bgfx::Init::resolution);
    Init.def_readwrite("limits", &bgfx::Init::limits);
    Init.def_readwrite("callback", &bgfx::Init::callback);
    Init.def_readwrite("allocator", &bgfx::Init::allocator);
    PYCLASS_END(libaimgfx, bgfx::Init, Init)


        PYCLASS_BEGIN(libaimgfx, bgfx::Memory, Memory)
    Memory.def(py::init<>());
    Memory.def_readwrite("data", &bgfx::Memory::data);
    Memory.def_readwrite("size", &bgfx::Memory::size);
    PYCLASS_END(libaimgfx, bgfx::Memory, Memory)


        PYCLASS_BEGIN(libaimgfx, bgfx::Caps, Caps)
    Caps.def_readwrite("renderer_type", &bgfx::Caps::rendererType);
    Caps.def_readwrite("supported", &bgfx::Caps::supported);
    Caps.def_readwrite("vendor_id", &bgfx::Caps::vendorId);
    Caps.def_readwrite("device_id", &bgfx::Caps::deviceId);
    Caps.def_readwrite("homogeneous_depth", &bgfx::Caps::homogeneousDepth);
    Caps.def_readwrite("origin_bottom_left", &bgfx::Caps::originBottomLeft);
    Caps.def_readwrite("num_gp_us", &bgfx::Caps::numGPUs);
    Caps.def_readonly("gpu", &bgfx::Caps::gpu);
    Caps.def_readwrite("limits", &bgfx::Caps::limits);
    Caps.def_readonly("formats", &bgfx::Caps::formats);
    PYCLASS_END(libaimgfx, bgfx::Caps, Caps)


        PYCLASS_BEGIN(libaimgfx, bgfx::TransientIndexBuffer, TransientIndexBuffer)
    TransientIndexBuffer.def_readwrite("data", &bgfx::TransientIndexBuffer::data);
    TransientIndexBuffer.def_readwrite("size", &bgfx::TransientIndexBuffer::size);
    TransientIndexBuffer.def_readwrite("start_index", &bgfx::TransientIndexBuffer::startIndex);
    TransientIndexBuffer.def_readwrite("handle", &bgfx::TransientIndexBuffer::handle);
    TransientIndexBuffer.def_readwrite("is_index16", &bgfx::TransientIndexBuffer::isIndex16);
    PYCLASS_END(libaimgfx, bgfx::TransientIndexBuffer, TransientIndexBuffer)


        PYCLASS_BEGIN(libaimgfx, bgfx::TransientVertexBuffer, TransientVertexBuffer)
    TransientVertexBuffer.def_readwrite("data", &bgfx::TransientVertexBuffer::data);
    TransientVertexBuffer.def_readwrite("size", &bgfx::TransientVertexBuffer::size);
    TransientVertexBuffer.def_readwrite("start_vertex", &bgfx::TransientVertexBuffer::startVertex);
    TransientVertexBuffer.def_readwrite("stride", &bgfx::TransientVertexBuffer::stride);
    TransientVertexBuffer.def_readwrite("handle", &bgfx::TransientVertexBuffer::handle);
    TransientVertexBuffer.def_readwrite("layout_handle", &bgfx::TransientVertexBuffer::layoutHandle);
    PYCLASS_END(libaimgfx, bgfx::TransientVertexBuffer, TransientVertexBuffer)


        PYCLASS_BEGIN(libaimgfx, bgfx::InstanceDataBuffer, InstanceDataBuffer)
    InstanceDataBuffer.def_readwrite("data", &bgfx::InstanceDataBuffer::data);
    InstanceDataBuffer.def_readwrite("size", &bgfx::InstanceDataBuffer::size);
    InstanceDataBuffer.def_readwrite("offset", &bgfx::InstanceDataBuffer::offset);
    InstanceDataBuffer.def_readwrite("num", &bgfx::InstanceDataBuffer::num);
    InstanceDataBuffer.def_readwrite("stride", &bgfx::InstanceDataBuffer::stride);
    InstanceDataBuffer.def_readwrite("handle", &bgfx::InstanceDataBuffer::handle);
    PYCLASS_END(libaimgfx, bgfx::InstanceDataBuffer, InstanceDataBuffer)


        PYCLASS_BEGIN(libaimgfx, bgfx::TextureInfo, TextureInfo)
    TextureInfo.def_readwrite("format", &bgfx::TextureInfo::format);
    TextureInfo.def_readwrite("storage_size", &bgfx::TextureInfo::storageSize);
    TextureInfo.def_readwrite("width", &bgfx::TextureInfo::width);
    TextureInfo.def_readwrite("height", &bgfx::TextureInfo::height);
    TextureInfo.def_readwrite("depth", &bgfx::TextureInfo::depth);
    TextureInfo.def_readwrite("num_layers", &bgfx::TextureInfo::numLayers);
    TextureInfo.def_readwrite("num_mips", &bgfx::TextureInfo::numMips);
    TextureInfo.def_readwrite("bits_per_pixel", &bgfx::TextureInfo::bitsPerPixel);
    TextureInfo.def_readwrite("cube_map", &bgfx::TextureInfo::cubeMap);
    PYCLASS_END(libaimgfx, bgfx::TextureInfo, TextureInfo)


        PYCLASS_BEGIN(libaimgfx, bgfx::UniformInfo, UniformInfo)
    UniformInfo.def_readonly("name", &bgfx::UniformInfo::name);
    UniformInfo.def_readwrite("type", &bgfx::UniformInfo::type);
    UniformInfo.def_readwrite("num", &bgfx::UniformInfo::num);
    PYCLASS_END(libaimgfx, bgfx::UniformInfo, UniformInfo)


        PYCLASS_BEGIN(libaimgfx, bgfx::Attachment, Attachment)
    Attachment.def("init", &bgfx::Attachment::init
    , py::arg("_handle")
    , py::arg("_access") = Access::Write
    , py::arg("_layer") = 0
    , py::arg("_num_layers") = 1
    , py::arg("_mip") = 0
    , py::arg("_resolve") = BGFX_RESOLVE_AUTO_GEN_MIPS
    , py::return_value_policy::automatic_reference);
    Attachment.def_readwrite("access", &bgfx::Attachment::access);
    Attachment.def_readwrite("handle", &bgfx::Attachment::handle);
    Attachment.def_readwrite("mip", &bgfx::Attachment::mip);
    Attachment.def_readwrite("layer", &bgfx::Attachment::layer);
    Attachment.def_readwrite("num_layers", &bgfx::Attachment::numLayers);
    Attachment.def_readwrite("resolve", &bgfx::Attachment::resolve);
    PYCLASS_END(libaimgfx, bgfx::Attachment, Attachment)


        PYCLASS_BEGIN(libaimgfx, bgfx::Transform, Transform)
    Transform.def_readwrite("data", &bgfx::Transform::data);
    Transform.def_readwrite("num", &bgfx::Transform::num);
    PYCLASS_END(libaimgfx, bgfx::Transform, Transform)


        PYCLASS_BEGIN(libaimgfx, bgfx::ViewStats, ViewStats)
    ViewStats.def_readonly("name", &bgfx::ViewStats::name);
    ViewStats.def_readwrite("view", &bgfx::ViewStats::view);
    ViewStats.def_readwrite("cpu_time_begin", &bgfx::ViewStats::cpuTimeBegin);
    ViewStats.def_readwrite("cpu_time_end", &bgfx::ViewStats::cpuTimeEnd);
    ViewStats.def_readwrite("gpu_time_begin", &bgfx::ViewStats::gpuTimeBegin);
    ViewStats.def_readwrite("gpu_time_end", &bgfx::ViewStats::gpuTimeEnd);
    PYCLASS_END(libaimgfx, bgfx::ViewStats, ViewStats)


        PYCLASS_BEGIN(libaimgfx, bgfx::EncoderStats, EncoderStats)
    EncoderStats.def_readwrite("cpu_time_begin", &bgfx::EncoderStats::cpuTimeBegin);
    EncoderStats.def_readwrite("cpu_time_end", &bgfx::EncoderStats::cpuTimeEnd);
    PYCLASS_END(libaimgfx, bgfx::EncoderStats, EncoderStats)


        PYCLASS_BEGIN(libaimgfx, bgfx::Stats, Stats)
    Stats.def_readwrite("cpu_time_frame", &bgfx::Stats::cpuTimeFrame);
    Stats.def_readwrite("cpu_time_begin", &bgfx::Stats::cpuTimeBegin);
    Stats.def_readwrite("cpu_time_end", &bgfx::Stats::cpuTimeEnd);
    Stats.def_readwrite("cpu_timer_freq", &bgfx::Stats::cpuTimerFreq);
    Stats.def_readwrite("gpu_time_begin", &bgfx::Stats::gpuTimeBegin);
    Stats.def_readwrite("gpu_time_end", &bgfx::Stats::gpuTimeEnd);
    Stats.def_readwrite("gpu_timer_freq", &bgfx::Stats::gpuTimerFreq);
    Stats.def_readwrite("wait_render", &bgfx::Stats::waitRender);
    Stats.def_readwrite("wait_submit", &bgfx::Stats::waitSubmit);
    Stats.def_readwrite("num_draw", &bgfx::Stats::numDraw);
    Stats.def_readwrite("num_compute", &bgfx::Stats::numCompute);
    Stats.def_readwrite("num_blit", &bgfx::Stats::numBlit);
    Stats.def_readwrite("max_gpu_latency", &bgfx::Stats::maxGpuLatency);
    Stats.def_readwrite("num_dynamic_index_buffers", &bgfx::Stats::numDynamicIndexBuffers);
    Stats.def_readwrite("num_dynamic_vertex_buffers", &bgfx::Stats::numDynamicVertexBuffers);
    Stats.def_readwrite("num_frame_buffers", &bgfx::Stats::numFrameBuffers);
    Stats.def_readwrite("num_index_buffers", &bgfx::Stats::numIndexBuffers);
    Stats.def_readwrite("num_occlusion_queries", &bgfx::Stats::numOcclusionQueries);
    Stats.def_readwrite("num_programs", &bgfx::Stats::numPrograms);
    Stats.def_readwrite("num_shaders", &bgfx::Stats::numShaders);
    Stats.def_readwrite("num_textures", &bgfx::Stats::numTextures);
    Stats.def_readwrite("num_uniforms", &bgfx::Stats::numUniforms);
    Stats.def_readwrite("num_vertex_buffers", &bgfx::Stats::numVertexBuffers);
    Stats.def_readwrite("num_vertex_layouts", &bgfx::Stats::numVertexLayouts);
    Stats.def_readwrite("texture_memory_used", &bgfx::Stats::textureMemoryUsed);
    Stats.def_readwrite("rt_memory_used", &bgfx::Stats::rtMemoryUsed);
    Stats.def_readwrite("transient_vb_used", &bgfx::Stats::transientVbUsed);
    Stats.def_readwrite("transient_ib_used", &bgfx::Stats::transientIbUsed);
    Stats.def_readonly("num_prims", &bgfx::Stats::numPrims);
    Stats.def_readwrite("gpu_memory_max", &bgfx::Stats::gpuMemoryMax);
    Stats.def_readwrite("gpu_memory_used", &bgfx::Stats::gpuMemoryUsed);
    Stats.def_readwrite("width", &bgfx::Stats::width);
    Stats.def_readwrite("height", &bgfx::Stats::height);
    Stats.def_readwrite("text_width", &bgfx::Stats::textWidth);
    Stats.def_readwrite("text_height", &bgfx::Stats::textHeight);
    Stats.def_readwrite("num_views", &bgfx::Stats::numViews);
    Stats.def_readwrite("view_stats", &bgfx::Stats::viewStats);
    Stats.def_readwrite("num_encoders", &bgfx::Stats::numEncoders);
    Stats.def_readwrite("encoder_stats", &bgfx::Stats::encoderStats);
    PYCLASS_END(libaimgfx, bgfx::Stats, Stats)


        PYCLASS_BEGIN(libaimgfx, bgfx::Encoder, Encoder)
    Encoder.def("set_marker", &bgfx::Encoder::setMarker
    , py::arg("_marker")
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_state", &bgfx::Encoder::setState
    , py::arg("_state")
    , py::arg("_rgba") = 0
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_condition", &bgfx::Encoder::setCondition
    , py::arg("_handle")
    , py::arg("_visible")
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_stencil", &bgfx::Encoder::setStencil
    , py::arg("_fstencil")
    , py::arg("_bstencil") = BGFX_STENCIL_NONE
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_scissor", py::overload_cast<uint16_t, uint16_t, uint16_t, uint16_t>(&bgfx::Encoder::setScissor)
    , py::arg("_x")
    , py::arg("_y")
    , py::arg("_width")
    , py::arg("_height")
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_scissor", py::overload_cast<uint16_t>(&bgfx::Encoder::setScissor)
    , py::arg("_cache") = UINT16_MAX
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_transform", py::overload_cast<const void *, uint16_t>(&bgfx::Encoder::setTransform)
    , py::arg("_mtx")
    , py::arg("_num") = 1
    , py::return_value_policy::automatic_reference);
    Encoder.def("alloc_transform", &bgfx::Encoder::allocTransform
    , py::arg("_transform")
    , py::arg("_num")
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_transform", py::overload_cast<uint32_t, uint16_t>(&bgfx::Encoder::setTransform)
    , py::arg("_cache")
    , py::arg("_num") = 1
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_uniform", &bgfx::Encoder::setUniform
    , py::arg("_handle")
    , py::arg("_value")
    , py::arg("_num") = 1
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_index_buffer", py::overload_cast<bgfx::IndexBufferHandle>(&bgfx::Encoder::setIndexBuffer)
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_index_buffer", py::overload_cast<bgfx::IndexBufferHandle, uint32_t, uint32_t>(&bgfx::Encoder::setIndexBuffer)
    , py::arg("_handle")
    , py::arg("_first_index")
    , py::arg("_num_indices")
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_index_buffer", py::overload_cast<bgfx::DynamicIndexBufferHandle>(&bgfx::Encoder::setIndexBuffer)
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_index_buffer", py::overload_cast<bgfx::DynamicIndexBufferHandle, uint32_t, uint32_t>(&bgfx::Encoder::setIndexBuffer)
    , py::arg("_handle")
    , py::arg("_first_index")
    , py::arg("_num_indices")
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_index_buffer", py::overload_cast<const bgfx::TransientIndexBuffer *>(&bgfx::Encoder::setIndexBuffer)
    , py::arg("_tib")
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_index_buffer", py::overload_cast<const bgfx::TransientIndexBuffer *, uint32_t, uint32_t>(&bgfx::Encoder::setIndexBuffer)
    , py::arg("_tib")
    , py::arg("_first_index")
    , py::arg("_num_indices")
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_vertex_buffer", py::overload_cast<uint8_t, bgfx::VertexBufferHandle>(&bgfx::Encoder::setVertexBuffer)
    , py::arg("_stream")
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_vertex_buffer", py::overload_cast<uint8_t, bgfx::VertexBufferHandle, uint32_t, uint32_t, bgfx::VertexLayoutHandle>(&bgfx::Encoder::setVertexBuffer)
    , py::arg("_stream")
    , py::arg("_handle")
    , py::arg("_start_vertex")
    , py::arg("_num_vertices")
    , py::arg("_layout_handle") = bgfx::VertexLayoutHandle(BGFX_INVALID_HANDLE)
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_vertex_buffer", py::overload_cast<uint8_t, bgfx::DynamicVertexBufferHandle>(&bgfx::Encoder::setVertexBuffer)
    , py::arg("_stream")
    , py::arg("_handle")
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_vertex_buffer", py::overload_cast<uint8_t, bgfx::DynamicVertexBufferHandle, uint32_t, uint32_t, bgfx::VertexLayoutHandle>(&bgfx::Encoder::setVertexBuffer)
    , py::arg("_stream")
    , py::arg("_handle")
    , py::arg("_start_vertex")
    , py::arg("_num_vertices")
    , py::arg("_layout_handle") = bgfx::VertexLayoutHandle(BGFX_INVALID_HANDLE)
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_vertex_buffer", py::overload_cast<uint8_t, const bgfx::TransientVertexBuffer *>(&bgfx::Encoder::setVertexBuffer)
    , py::arg("_stream")
    , py::arg("_tvb")
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_vertex_buffer", py::overload_cast<uint8_t, const bgfx::TransientVertexBuffer *, uint32_t, uint32_t, bgfx::VertexLayoutHandle>(&bgfx::Encoder::setVertexBuffer)
    , py::arg("_stream")
    , py::arg("_tvb")
    , py::arg("_start_vertex")
    , py::arg("_num_vertices")
    , py::arg("_layout_handle") = bgfx::VertexLayoutHandle(BGFX_INVALID_HANDLE)
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_vertex_count", &bgfx::Encoder::setVertexCount
    , py::arg("_num_vertices")
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_instance_data_buffer", py::overload_cast<const bgfx::InstanceDataBuffer *>(&bgfx::Encoder::setInstanceDataBuffer)
    , py::arg("_idb")
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_instance_data_buffer", py::overload_cast<const bgfx::InstanceDataBuffer *, uint32_t, uint32_t>(&bgfx::Encoder::setInstanceDataBuffer)
    , py::arg("_idb")
    , py::arg("_start")
    , py::arg("_num")
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_instance_data_buffer", py::overload_cast<bgfx::VertexBufferHandle, uint32_t, uint32_t>(&bgfx::Encoder::setInstanceDataBuffer)
    , py::arg("_handle")
    , py::arg("_start")
    , py::arg("_num")
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_instance_data_buffer", py::overload_cast<bgfx::DynamicVertexBufferHandle, uint32_t, uint32_t>(&bgfx::Encoder::setInstanceDataBuffer)
    , py::arg("_handle")
    , py::arg("_start")
    , py::arg("_num")
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_instance_count", &bgfx::Encoder::setInstanceCount
    , py::arg("_num_instances")
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_texture", &bgfx::Encoder::setTexture
    , py::arg("_stage")
    , py::arg("_sampler")
    , py::arg("_handle")
    , py::arg("_flags") = UINT32_MAX
    , py::return_value_policy::automatic_reference);
    Encoder.def("touch", &bgfx::Encoder::touch
    , py::arg("_id")
    , py::return_value_policy::automatic_reference);
    Encoder.def("submit", py::overload_cast<bgfx::ViewId, bgfx::ProgramHandle, uint32_t, uint8_t>(&bgfx::Encoder::submit)
    , py::arg("_id")
    , py::arg("_program")
    , py::arg("_depth") = 0
    , py::arg("_flags") = BGFX_DISCARD_ALL
    , py::return_value_policy::automatic_reference);
    Encoder.def("submit", py::overload_cast<bgfx::ViewId, bgfx::ProgramHandle, bgfx::OcclusionQueryHandle, uint32_t, uint8_t>(&bgfx::Encoder::submit)
    , py::arg("_id")
    , py::arg("_program")
    , py::arg("_occlusion_query")
    , py::arg("_depth") = 0
    , py::arg("_flags") = BGFX_DISCARD_ALL
    , py::return_value_policy::automatic_reference);
    Encoder.def("submit", py::overload_cast<bgfx::ViewId, bgfx::ProgramHandle, bgfx::IndirectBufferHandle, uint16_t, uint16_t, uint32_t, uint8_t>(&bgfx::Encoder::submit)
    , py::arg("_id")
    , py::arg("_program")
    , py::arg("_indirect_handle")
    , py::arg("_start") = 0
    , py::arg("_num") = 1
    , py::arg("_depth") = 0
    , py::arg("_flags") = BGFX_DISCARD_ALL
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_buffer", py::overload_cast<uint8_t, bgfx::IndexBufferHandle, Access::Enum>(&bgfx::Encoder::setBuffer)
    , py::arg("_stage")
    , py::arg("_handle")
    , py::arg("_access")
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_buffer", py::overload_cast<uint8_t, bgfx::VertexBufferHandle, Access::Enum>(&bgfx::Encoder::setBuffer)
    , py::arg("_stage")
    , py::arg("_handle")
    , py::arg("_access")
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_buffer", py::overload_cast<uint8_t, bgfx::DynamicIndexBufferHandle, Access::Enum>(&bgfx::Encoder::setBuffer)
    , py::arg("_stage")
    , py::arg("_handle")
    , py::arg("_access")
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_buffer", py::overload_cast<uint8_t, bgfx::DynamicVertexBufferHandle, Access::Enum>(&bgfx::Encoder::setBuffer)
    , py::arg("_stage")
    , py::arg("_handle")
    , py::arg("_access")
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_buffer", py::overload_cast<uint8_t, bgfx::IndirectBufferHandle, Access::Enum>(&bgfx::Encoder::setBuffer)
    , py::arg("_stage")
    , py::arg("_handle")
    , py::arg("_access")
    , py::return_value_policy::automatic_reference);
    Encoder.def("set_image", &bgfx::Encoder::setImage
    , py::arg("_stage")
    , py::arg("_handle")
    , py::arg("_mip")
    , py::arg("_access")
    , py::arg("_format") = TextureFormat::Count
    , py::return_value_policy::automatic_reference);
    Encoder.def("dispatch", py::overload_cast<bgfx::ViewId, bgfx::ProgramHandle, uint32_t, uint32_t, uint32_t, uint8_t>(&bgfx::Encoder::dispatch)
    , py::arg("_id")
    , py::arg("_handle")
    , py::arg("_num_x") = 1
    , py::arg("_num_y") = 1
    , py::arg("_num_z") = 1
    , py::arg("_flags") = BGFX_DISCARD_ALL
    , py::return_value_policy::automatic_reference);
    Encoder.def("dispatch", py::overload_cast<bgfx::ViewId, bgfx::ProgramHandle, bgfx::IndirectBufferHandle, uint16_t, uint16_t, uint8_t>(&bgfx::Encoder::dispatch)
    , py::arg("_id")
    , py::arg("_handle")
    , py::arg("_indirect_handle")
    , py::arg("_start") = 0
    , py::arg("_num") = 1
    , py::arg("_flags") = BGFX_DISCARD_ALL
    , py::return_value_policy::automatic_reference);
    Encoder.def("discard", &bgfx::Encoder::discard
    , py::arg("_flags") = BGFX_DISCARD_ALL
    , py::return_value_policy::automatic_reference);
    Encoder.def("blit", py::overload_cast<bgfx::ViewId, bgfx::TextureHandle, uint16_t, uint16_t, bgfx::TextureHandle, uint16_t, uint16_t, uint16_t, uint16_t>(&bgfx::Encoder::blit)
    , py::arg("_id")
    , py::arg("_dst")
    , py::arg("_dst_x")
    , py::arg("_dst_y")
    , py::arg("_src")
    , py::arg("_src_x") = 0
    , py::arg("_src_y") = 0
    , py::arg("_width") = UINT16_MAX
    , py::arg("_height") = UINT16_MAX
    , py::return_value_policy::automatic_reference);
    Encoder.def("blit", py::overload_cast<bgfx::ViewId, bgfx::TextureHandle, uint8_t, uint16_t, uint16_t, uint16_t, bgfx::TextureHandle, uint8_t, uint16_t, uint16_t, uint16_t, uint16_t, uint16_t, uint16_t>(&bgfx::Encoder::blit)
    , py::arg("_id")
    , py::arg("_dst")
    , py::arg("_dst_mip")
    , py::arg("_dst_x")
    , py::arg("_dst_y")
    , py::arg("_dst_z")
    , py::arg("_src")
    , py::arg("_src_mip") = 0
    , py::arg("_src_x") = 0
    , py::arg("_src_y") = 0
    , py::arg("_src_z") = 0
    , py::arg("_width") = UINT16_MAX
    , py::arg("_height") = UINT16_MAX
    , py::arg("_depth") = UINT16_MAX
    , py::return_value_policy::automatic_reference);
    PYCLASS_END(libaimgfx, bgfx::Encoder, Encoder)


        PYCLASS_BEGIN(libaimgfx, bgfx::VertexLayout, VertexLayout)
    VertexLayout.def(py::init<>());
    VertexLayout.def("begin", &bgfx::VertexLayout::begin
    , py::arg("_renderer") = RendererType::Noop
    , py::return_value_policy::reference);
    VertexLayout.def("end", &bgfx::VertexLayout::end
    , py::return_value_policy::automatic_reference);
    VertexLayout.def("add", &bgfx::VertexLayout::add
    , py::arg("_attrib")
    , py::arg("_num")
    , py::arg("_type")
    , py::arg("_normalized") = false
    , py::arg("_as_int") = false
    , py::return_value_policy::reference);
    VertexLayout.def("skip", &bgfx::VertexLayout::skip
    , py::arg("_num")
    , py::return_value_policy::reference);
    VertexLayout.def("has", &bgfx::VertexLayout::has
    , py::arg("_attrib")
    , py::return_value_policy::automatic_reference);
    VertexLayout.def("get_offset", &bgfx::VertexLayout::getOffset
    , py::arg("_attrib")
    , py::return_value_policy::automatic_reference);
    VertexLayout.def("get_stride", &bgfx::VertexLayout::getStride
    , py::return_value_policy::automatic_reference);
    VertexLayout.def("get_size", &bgfx::VertexLayout::getSize
    , py::arg("_num")
    , py::return_value_policy::automatic_reference);
    VertexLayout.def_readwrite("m_hash", &bgfx::VertexLayout::m_hash);
    VertexLayout.def_readwrite("m_stride", &bgfx::VertexLayout::m_stride);
    VertexLayout.def_readonly("m_offset", &bgfx::VertexLayout::m_offset);
    VertexLayout.def_readonly("m_attributes", &bgfx::VertexLayout::m_attributes);
    PYCLASS_END(libaimgfx, bgfx::VertexLayout, VertexLayout)



}

