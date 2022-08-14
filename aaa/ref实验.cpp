#include <iostream>
#include <string>
#include <type_traits>
using namespace std;

class C1
{
public:
  string a;
  C1(){
    this->a = "aaaaaaaaaaaaaaaaa";
    cout << "0 constructor called" << endl;
  }
  
  /*复制构造函数，不修改被拷贝的对象，所以参数为const；参数是引用，
    是因为如果不是引用，在传递参数的时候就会被调用复制构造函数，而这
    个函数本身就是复制构造函数，会造成无穷的递归调用
  */
  C1(const string &c){
    cout << "& constructor called"<< endl;
  }
  C1(string &&c){
    cout << "&& constructor called"<< endl;
  }
  C1(const C1 &c){
    this->a = c.a;
    cout << "copy constructor called"<< endl;
  }
  C1(C1 &&c){
    this->a = c.a;
    cout << "move constructor called"<< endl;
  }
  template<typename T>
  void operator= (T &&t){
    cout << "= called"<< endl;
  }
};
class C2
{
public:
  C1 c1;
  C2():c1(){
  }
  //直接返回c1必定会有复制损失
  //operator=和构造函数很相似,但type a=使用构造函数,a=使用operator=
  C1 &getC1(){
    //C1 c=C1(1);虽然是初始化后赋值,但编译器会优化为只赋值,不开优化也会被优化
    return c1;
  }
};
void f1(const string &s){
  printf("f1");
}
void f1(string &&s){
  printf("f2");
}
int main(){
  C1 a;//C1 a()声明了一个函数C1 a;才是无参构造
  a="ddawdawsas";
  C1 a0("daddawdawdwa");
  C1 a1(a0);
  C1 a2(C1("d"));
  C1 a3=a0;
  auto &&s=string{"adawdasdaadwdwa"};
  auto &&s0=("adawdasdaadwdwa");//auto &&为A16_c,auto为PKc,char *为Pc
  //生成了临时string对象,所以调用&&方法
  //传引用时全按左值处理...大概
  f1(s);
  f1(s0);
  std::cout<< typeid(s).name() <<std::endl;
  std::cout<< typeid(s0).name() <<std::endl;
  C1 a4=C1(s);
  C1 a5=C1(s0);
  C1 a6=C1(string("adawdasdaadwdwa"));
  cout << "***************************" <<endl;
  C2 c2;
  //不管cgetc1返回左值还是右值,都会调用复制构造函数,因为c1不是引用
  //此时给c1加引用只能＋右值,因为函数返回值不是左值,除非返回左值
  //此处应该是被优化过才只有一次复制
  //&&其实是const &的一种
  C1 c1 = c2.getC1();
  cout<<(&c1)<<endl<<(&c2.c1)<<endl;
  return 0;
}
