#include "head.cpp"
#include<stdio.h>

class Person{
public:
  virtual void p(){cout << "p()"<< endl;};
  ~Person(){cout<< "~Person"<< endl;};
  Person(){cout<< "Person"<< endl;};
};

void a(string s){
  cout<< s;
  getchar();
}
int main(){
  for(auto s : readline("txt")){
    a(s);
  }
  
  return 1;
}
