#include <iostream>
#include <vector>

int main() {
    std::vector<int> v;
    v.push_back(3);
    v.push_back(2);
    v.push_back(5);

    for (int i = 0; i < v.size(); i++) {
        std::cout << v[i] << "\n";
    }

    // A shorter way to iterate
    for (auto x : v) {
        std::cout << x << "\n";
    }

    return 0;
}

