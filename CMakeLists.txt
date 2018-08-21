CMAKE_MINIMUM_REQUIRED(VERSION 2.8.3)
INCLUDE(cmake/base.cmake)


SET(PROJECT_NAME pyrene-motions)
SET(PROJECT_DESCRIPTION "Motion sequence files for pyrene")
SET(PROJECT_URL "https://redmine.laas.fr/projects/pyrene-talos/repository/pyrene-motions")

SETUP_PROJECT()

FOREACH(dir grabHandrail15 identification multicontact15 multicontact15SingleStep multicontact15HalfStep climb15cmStairsNoHandrail)
  INSTALL(DIRECTORY ${CMAKE_SOURCE_DIR}/${dir}
    DESTINATION ${CMAKE_INSTALL_DATAROOTDIR}/${PROJECT_NAME})
ENDFOREACH(dir)

SETUP_PROJECT_FINALIZE()
