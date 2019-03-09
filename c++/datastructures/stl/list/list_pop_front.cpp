// http://www.cplusplus.com/reference/list/list/pop_front/
#include <iostream>
#include <list>

int main()
{
  std::list<int> mylist;
  mylist.push_front(300);
  mylist.push_front(200);
  mylist.push_front(100);

  std::cout << "Popping out the elements in mylist:";
  while (!mylist.empty()) {
    std::cout << " " << mylist.front();
    mylist.pop_front();
  }

  std::cout << "\nFinal size of mylist is " << mylist.size() << "\n";

  return 0;
}

