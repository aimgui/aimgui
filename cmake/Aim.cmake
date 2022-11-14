include_guard()

include(${CMAKE_CURRENT_LIST_DIR}/Standard.cmake)

function(USES_AIM THIS)
  USES_STANDARD(${THIS})
  target_include_directories(${THIS} PRIVATE
    ${AIM_ROOT}/pkg/aim/include
  )
endfunction()
