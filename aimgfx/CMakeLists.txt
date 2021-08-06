cmake_minimum_required(VERSION 3.4)

project(aimgfx VERSION "0.1")

include(../cmake/Common.cmake)

set(AIMGFX_DIR ${CMAKE_CURRENT_SOURCE_DIR})



pybind11_add_module(aimgfx MODULE
    src/aimgfx/bindings/init.cpp
)

configure_project(${PROJECT_NAME})

install(TARGETS aimgfx EXPORT aimgfx-targets
	LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
	ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
)
target_compile_definitions(aimgfx PRIVATE PRIxPTR="Ix")
#target_compile_definitions(aimgfx PRIVATE IMGUI_API=PYBIND11_EXPORT)
target_sources(aimgfx PRIVATE ${BGFX_SRC} ${BGFX_HEADERS} ${BX_SRC} ${BIMG_SRC})

# add include files
target_sources(aimgfx PRIVATE ${AIMGFX_INCLUDE}) # for intellisense
target_include_directories(aimgfx
	PUBLIC
		$<INSTALL_INTERFACE:include>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<BUILD_INTERFACE:${AIMGUI_DIR}/include>
        $<BUILD_INTERFACE:${IMGUI_DIR}>
        $<BUILD_INTERFACE:${BGFX_DIR}>
	PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src
)

#target_link_libraries(aimgfx PRIVATE Upstream::aimgui)
target_link_libraries(aimgfx PRIVATE astc-codec)

#
# INSTALL
#
# install headers
#install(DIRECTORY include/ DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
install(FILES ${BGFX_HEADERS} DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})


#install(TARGETS aimgfx DESTINATION .)
# Quiet a warning, since this project is only valid with SKBUILD
set(ignoreMe "${SKBUILD}")

#ADD_CUSTOM_COMMAND(TARGET aimgfx
#          POST_BUILD
#          #COMMAND ${CMAKE_COMMAND} -E make_directory ${PROJECT_BINARY_DIR}
#          COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_INSTALL_LIBDIR}/libaimgfx.so ./
#)