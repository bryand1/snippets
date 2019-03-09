// http://www.cplusplus.com/reference/map/map/at/
#include <iostream>
#include <string>
#include <map>

int main()
{
    std::map<std::string, int> mymap = {
        {"alpha", 0},
        {"beta", 0},
        {"gamma", 0},
    };

    mymap.at("alpha") = 10;
    mymap.at("beta") = 20;
    mymap["gamma"] = 30;  // Use bracket notation

    for (auto& x: mymap) {
        std::cout << x.first << ": " << x.second << "\n";
    }

    return 0;
}
