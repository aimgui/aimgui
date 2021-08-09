#pragma once

#include <pybind11/pybind11.h>

#include <bgfx/bgfx.h>
#include <bgfx/platform.h>

namespace py = pybind11;

struct AimGfxHandle {
  uint16_t idx;
  inline bool isValid() { return bgfx::kInvalidHandle != idx; }
};
