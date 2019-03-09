// http://www.cplusplus.com/reference/set/set/lower_bound/
// http://www.cplusplus.com/reference/set/set/upper_bound/
#include <iostream>
#include <set>

int main()
{
  std::set<int> myset;
  std::set<int>::iterator it_low, it_up;

  for (int i = 1; i < 10; i++) {
    myset.insert(i * 10);
  }

  it_low = myset.lower_bound(30);
  it_up = myset.upper_bound(60);

  myset.erase(it_low, it_up);

  std::cout << "myset contains:";
  for (std::set<int>::iterator it = myset.begin(); it != myset.end(); it++) {
    std::cout << " " << *it;
  }
  std::cout << "\n";

  return 0;
}

