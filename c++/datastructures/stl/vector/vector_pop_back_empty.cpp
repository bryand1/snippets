// http://www.cplusplus.com/reference/vector/vector/pop_back/
// http://www.cplusplus.com/reference/vector/vector/empty/
#include <iostream>
#include <vector>

int main()
{
  std::vector<int> myvector;
  myvector.push_back(100);
  myvector.push_back(200);
  myvector.push_back(300);

  int sum = 0;
  while (!myvector.empty()) {
    sum += myvector.back();
    myvector.pop_back();
  }

  std::cout << "The elements of myvector add up to " << sum << "\n";

  return 0;
}

