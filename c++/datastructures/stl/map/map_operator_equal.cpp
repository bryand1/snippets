#include <iostream>
#include <map>

int main()
{
  std::map<char, int> first;
  std::map<char, int> second;

  first['x'] = 8;
  first['y'] = 16;
  first['z'] = 32;

  second = first;
  first = std::map<char, int>();

  std::cout << "Size of first: " << first.size() << "\n";
  std::cout << "Size of second: " << second.size() << "\n";

  return 0;
}

