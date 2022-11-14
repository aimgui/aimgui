include_guard()

include(${CMAKE_CURRENT_LIST_DIR}/Standard.cmake)

function(USES_PYBIND11 THIS)
  USES_STANDARD(${THIS})
  target_include_directories(${THIS} PRIVATE
    ${PYBIND11_ROOT}/include()
  )
endfunction()

function(configure_project project)

set_target_properties(${project} PROPERTIES PREFIX "_")

if(CMAKE_COMPILER_IS_GNUCXX)
  set_target_properties(${project} PROPERTIES SUFFIX ".so")
else()
  set_target_properties(${project} PROPERTIES SUFFIX ".pyd")
endif(CMAKE_COMPILER_IS_GNUCXX)

endfunction()