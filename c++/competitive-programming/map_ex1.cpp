#include <iostream>
#include <map>

int main() {
    std::map<std::string,int> m;
    m["monkey"] = 4;
    m["banana"] = 3;
    m["harpsichord"] = 9;
    std::cout << m["banana"] << "\n";  // 3
    return 0;
}

