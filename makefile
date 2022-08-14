glflag=-lGL -lglfw -lGLEW -Wall
I=./lib
L=./lib
lib=my
flag=-I$(I) -L$(L) -l$(lib)
test:test.cpp
	g++ -std=c++2a  test.cpp -o test.exe $(flag)&&./test.exe
gl:opengl/opengl.cpp opengl/shader.cpp
	g++ opengl/opengl.cpp $(glflag) $(flag)
clean:
	rm ./test
