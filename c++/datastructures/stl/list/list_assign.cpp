// http://www.cplusplus.com/reference/list/list/assign/
#include <iostream>
#include <list>

int main()
{
  std::list<int> first;
  std::list<int> second;

  first.assign(7, 100);
  second.assign(first.begin(), first.end());

  int myints[] = {1776, 7, 4};
  first.assign(myints, myints + 3);

  std::cout << "Size of first: " << int(first.size()) << "\n";
  std::cout << "Size of second: " << int(second.size()) << "\n";
  return 0;
}

