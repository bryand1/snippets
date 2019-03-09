#include <iostream>
#include <list>

int main()
{
  std::list<int> mylist;
  std::list<int>::iterator it;

  mylist.push_back(200);
  mylist.push_back(300);
  mylist.push_front(100); // [ 100, 200, 300 ]

  std::cout << "mylist contains:";
  for (it = mylist.begin(); it != mylist.end(); ++it) {
    std::cout << " " << *it;
  }
  std::cout << "\n";

  mylist.clear();
  mylist.push_back(1101);
  mylist.push_back(2202);

  std::cout << "mylist contains:";
  for (auto &x: mylist) {
    std::cout << " " << x;
  }
  std::cout << "\n";
  return 0;
}

