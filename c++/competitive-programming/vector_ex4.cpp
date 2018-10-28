#include <iostream>
#include <string>

int main() {
    std::string a = "hatti";
    std::string b = a + a;
    std::cout << b << "\n";  // hattihatti
    b[5] = 'v';
    std::cout << b << "\n";  // hattivatti
    std::string c = b.substr(3, 4);
    std::cout << c << "\n";  // tiva
    return 0;
}

