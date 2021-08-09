cmake_minimum_required(VERSION 3.4)

project(aimapp VERSION "0.1")

include(../cmake/Common.cmake)

#GLFW BEGIN
set(GLFW_BUILD_DOCS OFF CACHE BOOL "" FORCE)
set(GLFW_BUILD_TESTS OFF CACHE BOOL "" FORCE)
set(GLFW_BUILD_EXAMPLES OFF CACHE BOOL "" FORCE)
add_subdirectory(${MONO_DIR}/glfw glfw)
#GLFW END

add_subdirectory(${CMAKE_CURRENT_SOURCE_DIR}/src/aimshell)

find_package(AimGui REQUIRED)
find_package(AimGfx REQUIRED)

set(AIMAPP_DIR ${MONO_DIR}/AIMAPP)

set(AIMAPP_HEADERS
)

set(AIMAPP_SRC
    #src/aimapp/bindings/glfw.cpp
    src/aimapp/bindings/main.cpp
)

pybind11_add_module(aimapp MODULE
    src/aimapp/bindings/init.cpp
)

configure_project(${PROJECT_NAME})

install(TARGETS aimapp EXPORT aimapp-targets
	LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
	ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
)
#target_compile_definitions(aimapp PRIVATE IMGUI_USER_CONFIG=<aimgui/aimconfig.h>)
target_sources(aimapp PRIVATE ${AIMAPP_SRC} ${AIMAPP_HEADERS})

# add include files
#target_sources(aimapp PRIVATE ${aimapp_INCLUDE}) # for intellisense
target_include_directories(aimapp
	PUBLIC
		$<INSTALL_INTERFACE:include>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<BUILD_INTERFACE:${AIMGUI_DIR}/include>
        $<BUILD_INTERFACE:${AIMGFX_DIR}/include>
        $<BUILD_INTERFACE:${AIMAPP_DIR}>
	PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src
        #"${GLFW_SOURCE_DIR}/src"
        #"${GLFW_BINARY_DIR}/src"
)

target_link_libraries(aimapp PRIVATE Upstream::aimgui Upstream::aimgfx)

#
# INSTALL
#
# install headers
#install(DIRECTORY include/ DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
install(FILES ${AIMAPP_HEADERS} DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})


#install(TARGETS aimapp DESTINATION .)
# Quiet a warning, since this project is only valid with SKBUILD
set(ignoreMe "${SKBUILD}")

#ADD_CUSTOM_COMMAND(TARGET aimapp
#          POST_BUILD
#          #COMMAND ${CMAKE_COMMAND} -E make_directory ${PROJECT_BINARY_DIR}
#          COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_INSTALL_LIBDIR}/libaimapp.so ./
#)