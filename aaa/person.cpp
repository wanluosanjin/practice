
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

class Person{
public:
  virtual void p(){cout << "p()"<< endl;};
  ~Person(){cout<< "~Person"<< endl;};
  template <typename T>Person (T&& t){cout<< "PersonT&&"<< endl;}
  Person(){cout<< "Person"<< endl;};
};

void a(string s){
  cout<< s;
  getchar();
}
Person b(){
  Person a{};
  return a;
}
int main(){
  //  for(auto s : readline("txt")){
  //    a(s);
  //}
  Person p{};
  Person&& c=b();
  Person a = b();
  cout<< "end"<< endl;
  return 1;
}
