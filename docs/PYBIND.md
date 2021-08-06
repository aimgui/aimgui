## I had to do this earlier, but now it's working?  Weird

#set_property(
#  TARGET pybind11::module
#  APPEND
#  PROPERTY
#    INTERFACE_LINK_LIBRARIES pybind11::python_link_helper
#    "$<$<OR:$<PLATFORM_ID:Windows>,$<PLATFORM_ID:Cygwin>>:$<BUILD_INTERFACE:${PYTHON_LIBRARIES}>>")

target_link_libraries(pybind11::module INTERFACE ${PYTHON_LIBRARIES})
