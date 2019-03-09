// http://www.cplusplus.com/reference/vector/vector/data/
#include <iostream>
#include <vector>

int main()
{
  std::vector<int> myvector(5);

  int *p = myvector.data();

  *p = 10;
  ++p;
  *p = 20;
  p[2] = 100;
  *(p + 3) = 999;

  std::cout << "myvector contains:";
  for (unsigned i = 0; i < myvector.size(); i++) {
    std::cout << " " << myvector[i];
  }
  std::cout << "\n";

  return 0;
}

