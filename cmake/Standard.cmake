cmake_minimum_required(VERSION 3.14)

include_guard()

include(${CMAKE_CURRENT_LIST_DIR}/Config.cmake)

function(USES_STANDARD THIS)
  #target_compile_definitions(${THIS} UNICODE _UNICODE)
  #target_compile_features(${THIS} PUBLIC cxx_std_17)
  target_compile_definitions(${THIS} PRIVATE NULL=nullptr)
  target_compile_features(${THIS} PUBLIC cxx_std_20)
  set_property(TARGET ${THIS} PROPERTY CXX_STANDARD 20)
  if ((MSVC) AND (MSVC_VERSION GREATER_EQUAL 1914))
    target_compile_options(${THIS} PRIVATE "/Zc:__cplusplus")
  endif()
  if (MSVC)
    target_compile_options(${THIS} PRIVATE /bigobj)
  endif ()
endfunction()

