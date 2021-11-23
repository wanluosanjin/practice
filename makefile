glflag=-lGL -lglfw -lGLEW -Wall
I=./lib
L=./lib
lib=my
flag=-I$(I) -L$(L) -l$(lib)
all:opengl.cpp shader.cpp
	g++ opengl.cpp $(glflag) $(flag)
test:test.cpp
	g++  test.cpp -o test.exe $(flag)
clean:
	rm ./test
