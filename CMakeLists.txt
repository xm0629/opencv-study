cmake_minimum_required(VERSION 2.8)

project(opencv-study)


set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

add_executable(${PROJECT_NAME} main-03-test.cpp)
target_link_libraries(${PROJECT_NAME} opencv_core opencv_highgui opencv_imgcodecs)
