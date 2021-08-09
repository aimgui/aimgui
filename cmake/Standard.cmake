cmake_minimum_required(VERSION 3.14)

include_guard()

include(${CMAKE_CURRENT_LIST_DIR}/Config.cmake)

function(USES_STANDARD THIS)
  #target_compile_definitions(${THIS} UNICODE _UNICODE)
  target_compile_features(${THIS} PUBLIC cxx_std_17)
  #target_compile_features(${THIS} PUBLIC cxx_std_20)
endfunction()

