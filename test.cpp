#include <map>
#include <type_traits>
#include <functional>
#include <string>
#include <iostream>
#include <typeinfo>
#include <any>
#include <variant>

#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>

#include "myhead.h"


//折叠表达式
//范围foreach
int main(){
    // USE_STD_ALIAS;
    // SV s="aaaa";
    // S a=" USE_STD_ALIAS ";
    using std::string ;
    string a="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
    auto b=123;

    std::vector<string> map{};
    std::cout << &a <<";" <<  (size_t)a.data()<<";";
    map.push_back(std::move(a));
    auto d=std::move(b);
    std::cout << &a <<";"<< &(map[0]) <<  (size_t)a.data()<<";"<<(size_t)map[0].data();
}
