#pragma once
#pragma message("加载head.cpp")
#pragma message("使用了namespace")

//   #pragma comment(lib, "user32.lib")
//该指令用来将user32.lib 库文件加入到本工程中。
//字，双字，和四字在自然边界上不需要在内存中对齐,无论如何，为了提高程序的性能，数据结构（尤其是栈）应该尽可能地在自然边界上对齐。原因在于，为了访问未对齐的内存，处理器需要作两次内存访问；然而，对齐的内存访问仅需要一次访问。

#include <stdio.h>
#include <type_traits>
#include <sys/types.h>
#include <dirent.h>
#include <unistd.h>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>

using namespace std;

void appendfile(const string& filepath,const string& content){
  ofstream outfile(filepath,ios::app);
  outfile << content;
  outfile.close();
}

inline string readfile(const string& filename) {
  ifstream in(filename);
  //另外有的程序员使用 ifstream 读取文件内容，然后直接赋值给std::string对象，肯定是错误的。因为：读取的char*类型赋值给string时，默认遇到 \0 就会结束，会丢弃后面的字符。
  //content((istreambuf_iterator<char>(in)), istreambuf_iterator<char>());
  istreambuf_iterator<char> begin(in), end;
  string content(begin, end);
  in.close();
  return content;
}

vector<string> readline(const string& path){
  ifstream in(path);
  string line;
  vector<string> vs;
  while (getline (in, line)) // line中不包括每行的换行符
    {
      vs.push_back(line);
    }
  in.close();
  return vs;
}

vector<string> listfile (const string& path)
{
  DIR    *dir;
  dirent    *ptr;
  vector<string> vs;
  dir = opendir(path.c_str()); ///open the dir

  while((ptr = readdir(dir)) != NULL) ///read the list of this dir
    {
      vs.push_back(ptr->d_name);
    }
  closedir(dir);
  return vs;
}

//t应该是vector,此方法有待完善
//requires和concept只能在-fconcept下使用
template<class t=vector<string>>
void printvector (t&& vs)
{
  for(int i=0;i<vs.size(); i++){
    cout << vs.at(i) << endl;
  }
}
void printvector (vector<string>* vs){
  for(int i=0;i<(*vs).size(); i++){
    cout << vs->at(i) << endl;
  }
}
