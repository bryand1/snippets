// http://www.cplusplus.com/reference/array/array/front/
// http://www.cplusplus.com/reference/array/array/back/
#include <iostream>
#include <array>

int main()
{

  std::array<int, 3> myarray = {2, 16, 77};
  std::cout << "front is: " << myarray.front() << std::endl;
  std::cout << "back is: " << myarray.back() << std::endl;
  myarray.front() = 100;
  std::cout << "myarray now contains:";
  for (int x: myarray) std::cout << " " << x;
  std::cout << "\n";
  return 0;
}

