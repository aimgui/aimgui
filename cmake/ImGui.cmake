include_guard()

function(USES_IMGUI THIS)
  target_compile_definitions(${THIS} PRIVATE IMGUI_USER_CONFIG=<aimgui/aimconfig.h>)
  target_include_directories(${THIS} PRIVATE
    ${IMGUI_ROOT}
    ${IMGUI_EX}
    ${FAUSTY_ROOT}/src
  )
  target_link_libraries(${THIS} ImGui)

endfunction()