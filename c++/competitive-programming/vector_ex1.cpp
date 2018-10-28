#include <iostream>
#include <vector>

int main() {
    std::vector<int> v;
    v.push_back(3);
    v.push_back(2);
    v.push_back(5);

    std::cout << v[0] << "\n";
    std::cout << v[1] << "\n";
    std::cout << v[2] << "\n";

    return 0;
}

