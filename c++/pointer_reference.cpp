// https://stackoverflow.com/questions/5789806/meaning-of-and-in-c
#include <iostream>
using namespace std;

void foo(int* ptr)
{
    ptr = new int(50);
    cout << "In foo:\t" << *ptr << "\n";
    delete ptr;
}

void bar(int*& ptr)
{
    ptr = new int(80);
    cout << "In bar:\t" << *ptr << "\n";
    // Deleting the pointer will result in the actual passed parameter dangling
}

int main()
{
    int temp = 100;
    int *p = &temp;

    cout << "Before foo:\t" << *p << "\n";
    foo(p);
    cout << "After too\t" << *p << "\n";

    cout << "Before bar:\t" << *p << "\n";
    bar(p);
    cout << "After bar:\t" << *p << "\n";

    delete p;

    return 0;
}

