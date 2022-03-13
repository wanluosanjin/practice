#include <map>
#include <functional>
#include <string>
#include <iostream>
#include <typeinfo>

#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>

#include "myhead.h"

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

class Test{
    public:
    template<class T>
    Test(T&& t){
        std::cout<< "Test:"<<typeid(t).name() <<std::endl;
        printTest();
    }
    Test(){
        std::cout<< "Test:()" <<std::endl;
        printTest();
    }
    template<class T>
    Test operator=(T&& t){
        std::cout<< "operator=:"<<typeid(t).name() <<std::endl;
        printTest();
        return t;
    }

    void printTest(){
        std::cout<< this << "string.data():"<<(void *)s.data()<<std::endl;
    }

    int i=233;
    string s="aaaaaaaaaaaaaaaaaaaaaaaaaaa";
};

//需要显性的将size_t转char*,char*会直接输出字符串
Test returnTest(){
    string b="bbbbbbbbbbbbbbbbbbb";
    Test a="aaaaaaaaaaaaaaaaaaaaaaaaaaaa";
    // std::cout<< &a <<std::endl;//调用两次,&b位置不变,&a位置改变并作为返回值,并继续增长
    return a;
}



int main(){
    // map<string,function<FactoryBase*(...)>> factory;
    Test a1=returnTest();//函数返回值没有开销,c++11已经优化了,左值会调用构造函数
    auto&& a2(returnTest());//复制构造也可以引用
    // a1=returnTest()+"1";//此处&a1不变,数据改变
    Test aaaaaaaaa=Test();
    aaaaaaaaa=Test();//这句不调用=(),算构造,只是同名
    std::cout<< (int)aaa<long,44>() <<std::endl;
    Test bbbbbbbbb;
    std::cout<< sizeof(aaa<int,44>()) <<std::endl;
    bbbbbbbbb=aaaaaaaaa;//=()参数引用,返回值非引用,返回引用构造临时变量,有一次复制
    std::cout<< typeid(aaa<long,44>::value_type).name() <<std::endl;
    std::cout<< (aaa<int,44>()()) <<std::endl;
    std::cout<< typeid(long).name() <<std::endl;
    std::cout<< typeid(55).name() <<std::endl;
    std::cout<< typeid(std::cout).name() <<std::endl;
    std::cout<< typeid(std::string).name() <<std::endl;
    std::cout<< typeid(Test).name() <<std::endl;
}