#include <iostream>
#include <vector>

int main() {
    std::vector<int> v;
    v.push_back(5);
    v.push_back(2);
    std::cout << v.back() << "\n"; // 2
    v.pop_back();
    std::cout << v.back() << "\n"; // 5

    std::vector<int> y = {2, 4, 2, 5, 1};

    // size 10, initial value 0
    std::vector<int> z(10);

    // size 10, initial value 5
    std::vector<int> w(10, 5);

    return 0;
}

