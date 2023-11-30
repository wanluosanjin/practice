#pragma once

#include "resource.h"

typedef size_t u64;
using u32 = UINT32;
using string = std::string;
using sv = std::string_view;
using iv = std::vector<int>;
using ssmap = std::unordered_map<sv, sv>;
auto f(auto&& a) {
	return a + a;
}
auto lambda0 = [](auto&& a) {return a + a;};
using sfmap = std::unordered_map < string, std::function < std::remove_pointer_t<decltype(+[](int){}) > > > ;
//using spmap = std::unordered_map < string, decltype([](auto&& a)static {return a + a;}) > ;//可以编译通过,但不能用?
using spmap = std::unordered_map < string, decltype(lambda0) > ;//可以编译通过,但不能用?