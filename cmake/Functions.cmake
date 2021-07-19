function(configure_project project)

set_target_properties(${project} PROPERTIES PREFIX "lib")

if(CMAKE_COMPILER_IS_GNUCXX)
  set_target_properties(${project} PROPERTIES SUFFIX ".so")
else()
  set_target_properties(${project} PROPERTIES SUFFIX ".pyd")
endif(CMAKE_COMPILER_IS_GNUCXX)

endfunction()