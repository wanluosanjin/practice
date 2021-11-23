glflag=-lGL -lglfw -lGLEW -Wall
I=./lib
L=./lib
lib=my
flag=-I$(I) -L$(L) -l$(lib)
test:test.cpp
	g++  test.cpp -o test.exe $(flag)&&./test.exe
gl:opengl.cpp shader.cpp
	g++ opengl.cpp $(glflag) $(flag)
clean:
	rm ./test
