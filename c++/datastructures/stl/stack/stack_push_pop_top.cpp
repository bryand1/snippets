// http://www.cplusplus.com/reference/stack/stack/push/
// http://www.cplusplus.com/reference/stack/stack/pop/
#include <iostream>
#include <stack>

int main()
{
  std::stack<int> mystack;

  for (int i = 0; i < 5; i++) mystack.push(i);

  std::cout << "Popping elements...";
  while (!mystack.empty()) {
    std::cout << " " << mystack.top();
    mystack.pop();
  }
  std::cout << "\n";
  return 0;
}
