#pragma message "编译aaa.cpp"
//#pragma once
//#pragma comment ( lib,"wpcap.lib" )  
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stddef.h>

#include <iostream>
#include <fstream>
#include <memory>
#include <algorithm>
#include <vector>
#include <string>

#include <type_traits>
#include <sys/types.h>
#include <dirent.h>
#include <unistd.h>

//某些头文件已经被其他头文件包含,比如utility,不用include
typedef unsigned char b;
typedef size_t u32;

using namespace std;

class Buffer{
public :
  template <typename s=string>
  Buffer(s&& name,size_t size):name(forward<string>(name)),size(size){
    buffer = malloc(size);
    if( buffer == NULL )
    {
      fprintf(stderr, "Error - unable to allocate required memory\n");
    }
  }
  Buffer(){};
  void Del(){
    free(buffer);
  }
  string name;
  size_t size;
  void *buffer=NULL;
};
class BufferCenter{
public :
  void addBuffer();
  Buffer getBuffer();
  void killBuffer();
  BufferCenter(){
  }
private :
  vector<Buffer> bufferVector{vector<Buffer>(128)};
};
  

class Book{
public :
  u32 id;
  std::string name;
  std::string teacher;
  float price;
  //不加{}编译器不会出错,但ld会undefined reference to `Book::Book()...{}是赋值
  Book(){};
  Book(u32 id):id(id){};
  ~Book(){cout<<"del Book"<<id<<endl;};
  template<typename temp1=string,typename temp2=string>
  Book(u32 id,temp1&& name,temp2&& teacher):id(id),name(forward<temp1>(name)),teacher(forward<temp2>(teacher)){cout<<"new Book"<<id<<endl;};
  /*复制构造函数，不修改被拷贝的对象，所以参数为const；参数是引用，
    是因为如果不是引用，在传递参数的时候就会被调用复制构造函数，而这
    个函数本身就是复制构造函数，会造成无穷的递归调用
  */
  Book(const Book& b){this->id=b.id;cout<<"copy Book"<<id<<endl;};
};

//string 未初始化什么也不输出
int main(){
  Book a(1,"a","aaa");
  Book b(a);
  b.name="bbb";
  cout<<a.name<<endl;
  cout<<b.name<<endl;
  int c;
  while(c = getchar() !=  EOF)
    putchar(c);
  return 0;
      
}
int temp2(){
  //vector默认值初始化时对象要包含默认构造函数,不过写了依旧出错
  //new 1 copy 1 输出0 在外面声明del 2,在里面声明del 1,筛选不输出
  unique_ptr<vector<Book>> a(new vector<Book>(8));
  a->push_back(*(new Book(3)));
  a->push_back(*(new Book(1)));
  a->push_back(*(new Book(2)));
  a->push_back(*(new Book(4)));

  sort(a->begin(),a->end(),[](Book& a,Book& b){return a.id<b.id;});
  auto it=find_if(a->begin(),a->end(),[](Book& a){return a.id==3;});
  //没有找到此句输出0
  cout<< it->id <<endl;
  return 0;
}
void temp1()
{
  b *description;

  /* 动态分配内存 */
  description = (b*)malloc( 30 * sizeof(b) );
  if( description == NULL )
    {
      fprintf(stderr, "Error - unable to allocate required memory\n");
    }
  else
                                                                                                                                              {
      *description = 0x32;
      description++;
      *description = 0x31;
      description--;
      
    }
  printf("Description: %s\n", description );

  /* 使用 free() 函数释放内存 */
  free(description);
}
