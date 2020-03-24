CMAKE_MINIMUM_REQUIRED(VERSION 3.1)

# Project properties
SET(PROJECT_ORG pyrene-dev)
SET(PROJECT_NAME pyrene-motions)
SET(PROJECT_DESCRIPTION "Motion sequence files for pyrene")
SET(PROJECT_URL "https://gepgitlab.laas.fr/${PROJECT_ORG}/${PROJECT_NAME}")

# Project configuration
SET(PROJECT_USE_CMAKE_EXPORT TRUE)

# JRL-cmakemodule setup
INCLUDE(cmake/base.cmake)

# Project definition
COMPUTE_PROJECT_ARGS(PROJECT_ARGS LANGUAGES CXX)
PROJECT(${PROJECT_NAME} ${PROJECT_ARGS})

ADD_LIBRARY(${PROJECT_NAME} INTERFACE)
INSTALL(TARGETS ${PROJECT_NAME} EXPORT ${TARGETS_EXPORT_NAME} DESTINATION lib)

FOREACH(dir grabHandrail15 identification multicontact15 multicontact15SingleStep multicontact15HalfStep climb15cmStairsNoHandrail)
  INSTALL(DIRECTORY ${dir} DESTINATION share/${PROJECT_NAME})
ENDFOREACH(dir)
