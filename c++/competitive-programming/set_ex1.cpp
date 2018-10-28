#include <iostream>
#include <set>

int main() {
    std::set<int> s;
    s.insert(3);
    s.insert(2);
    s.insert(5);
    std::cout << s.count(3) << "\n";  // 1
    std::cout << s.count(4) << "\n";  // 0
    s.erase(3);
    s.insert(4);
    std::cout << s.count(3) << "\n";  // 0
    std::cout << s.count(4) << "\n";  // 1

    // A set can be used mostly like a vector, but it is not possible to access the
    // elements using the [] notation. The following code creates a set, prints the
    // number of elements in it, and then iterates through all the elements.
    std::set<int> t = {2, 5, 6, 8};
    std::cout << t.size() << "\n"; // 4
    for (auto x : t) {
        std::cout << x << "\n";
    }
    return 0;
}

