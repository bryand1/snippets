#include <iostream>
#include <set>

int main() {
    std::multiset<int> s;
    s.insert(5);
    s.insert(5);
    s.insert(5);
    std::cout << s.count(5) << "\n";  // 3

    s.erase(5);
    std::cout << s.count(5) << "\n";  // 0


    s.insert(5);
    s.insert(5);
    s.insert(5);

    // If only one instance should be removed, it can be done as follows:
    s.erase(s.find(5));
    std::cout << s.count(5) << "\n"; // 2

    return 0;
}

