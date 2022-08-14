#pragma message "编译aaa.cpp"
//#pragma once
//#pragma comment ( lib,"wpcap.lib" )  
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stddef.h>

#include <map>
#include <functional>
#include <typeinfo>
#include <any>
#include <variant>
#include <iostream>
#include <fstream>
#include <memory>
#include <algorithm>
#include <vector>
#include <string>
#include <type_traits>

#include <sys/types.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <dirent.h>
#include <unistd.h>

#include "myhead.h"
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

using namespace std;

template <typename T>
class Singleton{
    public:
    static T& getInstance(){
        static T instance;
        return instance;
    }
};

template <typename T,T v>
struct aaa{
    static constexpr T value=v;
    typedef T value_type;
    typedef aaa<T,v> type;
    constexpr value_type operator()() const noexcept {return 1;}
    //类型转换函数
    constexpr operator value_type() const noexcept {return 2;}
};

#define printcharp(x)     do{char *p=(char *)(&x);std::cout<< p <<std::endl;}while(0); 
#define printp(x)     do{std::cout<< &x <<std::endl;}while(0); 
#define printl(x)     do{std::cout<<"line:"<< __LINE__<<std::endl << x <<std::endl;}while(0); 




template<typename Function>
class ScopeGuard {
    public:
    ScopeGuard(Function iFunc) {
        mFunc = iFunc;
    }
    ~ScopeGuard() {
        std::cout<<"Exit the scope, so run the scope guard.\n";
        (mFunc)();
    }
    private:
    Function mFunc;
};
const int& getRef(const int* p) { return *p; }
static_assert(std::is_same_v<decltype(getRef), const int&(const int*)>);
auto getRefFwdBad(const int* p) { return getRef(p); }
static_assert(std::is_same_v<decltype(getRefFwdBad), int(const int*)>,
    "Just returning auto isn't perfect forwarding.");
decltype(auto) getRefFwdGood(const int* p) { return getRef(p); }
static_assert(std::is_same_v<decltype(getRefFwdGood), const int&(const int*)>,
    "Returning decltype(auto) perfectly forwards the return type.");
 
// Alternatively:
auto getRefFwdGood1(const int* p) -> decltype(getRef(p)) { return getRef(p); }
static_assert(std::is_same_v<decltype(getRefFwdGood1), const int&(const int*)>,
    "Returning decltype(return expression) also perfectly forwards the return type.");
int main() {
    int i = 3;

    ScopeGuard<std::function<void()>> lGuard{([&]() {
        std::cout<<"access value "<<i <<std::endl;
    })};
    return 0;
}

/*

//typeid与构造函数实验
int main(){
    // map<string,function<FactoryBase*(...)>> factory;
    Test a1=returnTest();//函数返回值没有开销,c++11已经优化了,左值会调用构造函数
    auto&& a2(a1);//引用不复制
    auto a3(a1);
    printl(__DATE__ <<__TIME__<<__STDC__<<_SC_VERSION<<__STDC_HOSTED__<<__cplusplus)
    printl(typeid(a1).name())
    printl(typeid(a2).name())
    // a1=returnTest()+"1";//此处&a1不变,数据改变
    Test aaaaaaaaa=Test();
    aaaaaaaaa=Test();//这句不调用=(),算构造,只是同名
    Test bbbbbbbbb;
    bbbbbbbbb=aaaaaaaaa;//=()参数引用,返回值非引用,返回引用构造临时变量,有一次复制
    std::cout<< (int)aaa<long,44>() <<std::endl;
    std::cout<< sizeof(aaa<int,44>()) <<std::endl;
    std::cout<< typeid(aaa<long,44>::value_type).name() <<std::endl;
    std::cout<< (aaa<int,44>()()) <<std::endl;
    std::cout<< typeid(long).name() <<std::endl;
    std::cout<< typeid(55).name() <<std::endl;
    std::cout<< typeid(std::cout).name() <<std::endl;
    std::cout<< typeid(std::string).name() <<std::endl;
    std::cout<< typeid(Test).name() <<std::endl;
    static auto anyone = [](auto&& k, auto&&... args) ->bool { return ((args == k) || ...); };
    if(anyone('x','x','X','e','E','.')){
        std::cout<< "if" <<std::endl;;
    }
}
*/