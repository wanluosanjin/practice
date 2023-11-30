#include <concepts>
#include <future>
#include <ranges>
#include <functional>
#include <filesystem>


typedef size_t u64;
using u32 = uint32_t;
using string = std::string;
using sv = std::string_view;
using iv = std::vector<int>;

using ssmap = std::unordered_map<sv, sv>;
auto f(auto&& a) {
	return a + a;
}
auto lambda0 = [](auto&& a) {return a + a;};
using sfmap = std::unordered_map < string, std::function < std::remove_pointer_t<decltype(+[](int) {}) > > > ;
//using spmap = std::unordered_map < string, decltype([](auto&& a)static {return a + a;}) > ;//可以编译通过,但不能用?
using spmap = std::unordered_map < string, decltype(lambda0) >;

class oto {
	object* send;
	object* get;
	void  (* fn)(object*, object*);

};


template <typename ... ts>
class aaa:ts... {
	using ts::operatator()...
	public aaa(ts...) :ts()...{};
//	void  operator()(){};
};

//auto a= aaa {[]() {return 1;} };
using somap = std::unordered_map<sv, std::function<void(object*)>>;
class tag {
	somap so;
};
using stmap = std::unordered_map<sv, tag>;
class object {
	stmap ts;
	std::vector < std::function<object*> > gettagvec;
	std::vector < std::function<object*> > rmtagvec;
	void addtag(tag t);
	void rmtag(tag t);
	void hastag(tag t);
};