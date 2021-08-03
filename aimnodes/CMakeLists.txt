cmake_minimum_required(VERSION 3.4)

project(aimnodes VERSION "0.1")

include(../cmake/Common.cmake)

find_package(AimGui REQUIRED)

set(IMNODES_DIR ${MONO_DIR}/imnodes)

set(IMNODES_HEADERS
    ${IMNODES_DIR}/imnodes.h
    ${IMNODES_DIR}/imnodes_internal.h
)

set(IMNODES_SRC
    src/aimnodes/bindings/generated.cpp
    src/aimnodes/bindings/main.cpp
    ${IMNODES_DIR}/imnodes.cpp
)

pybind11_add_module(aimnodes MODULE
    src/aimnodes/bindings/init.cpp
)

configure_project(${PROJECT_NAME})

install(TARGETS aimnodes EXPORT aimnodes-targets
	LIBRARY DESTINATION ${CMAKE_INSTALL_LIBDIR}
	ARCHIVE DESTINATION ${CMAKE_INSTALL_LIBDIR}
)

target_sources(aimnodes PRIVATE ${IMNODES_SRC} ${IMNODES_HEADERS})

# add include files
target_sources(aimnodes PRIVATE ${AIMNODES_INCLUDE}) # for intellisense
target_include_directories(aimnodes
	PUBLIC
		$<INSTALL_INTERFACE:include>
        $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
        $<BUILD_INTERFACE:${AIMGUI_DIR}/include>
        $<BUILD_INTERFACE:${IMGUI_DIR}>
        $<BUILD_INTERFACE:${IMNODES_DIR}>
	PRIVATE
        ${CMAKE_CURRENT_SOURCE_DIR}/src
)

target_link_libraries(aimnodes PRIVATE Upstream::aimgui)

#
# INSTALL
#
# install headers
#install(DIRECTORY include/ DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})
install(FILES ${IMNODES_HEADERS} DESTINATION ${CMAKE_INSTALL_INCLUDEDIR})


#install(TARGETS aimnodes DESTINATION .)
# Quiet a warning, since this project is only valid with SKBUILD
set(ignoreMe "${SKBUILD}")

#ADD_CUSTOM_COMMAND(TARGET aimnodes
#          POST_BUILD
#          #COMMAND ${CMAKE_COMMAND} -E make_directory ${PROJECT_BINARY_DIR}
#          COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_INSTALL_LIBDIR}/libaimnodes.so ./
#)