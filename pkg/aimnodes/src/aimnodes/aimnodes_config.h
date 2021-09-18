#pragma once

#include <pybind11/functional.h>
namespace py = pybind11;

#define ImNodesMiniMapNodeHoveringCallback py::function
#define ImNodesMiniMapNodeHoveringCallbackDefault py::none()

#define ImNodesMiniMapNodeHoveringCallbackUserData py::object
#define ImNodesMiniMapNodeHoveringCallbackUserDataDefault py::none()