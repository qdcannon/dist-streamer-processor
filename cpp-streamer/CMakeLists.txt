cmake_minimum_required(VERSION 3.10)
project(MyImageCVApp)

# C++ Standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Find OpenCV
find_package(OpenCV REQUIRED)

# Include our headers
include_directories(${PROJECT_SOURCE_DIR}/include)
include_directories(${PROJECT_SOURCE_DIR}/lib)

include_directories(${OpenCV_INCLUDE_DIRS})

# Add the executable and source files
add_executable(${PROJECT_NAME}
    src/image_cv.cpp
    #src/image_utils.cpp
)

# Link OpenCV libraries
target_link_libraries(${PROJECT_NAME} ${OpenCV_LIBS})

# Optional: print OpenCV version
message(STATUS "Found OpenCV version: ${OpenCV_VERSION}")
