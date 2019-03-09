// http://www.cplusplus.com/reference/map/map/begin/
#include <iostream>
#include <map>
int main()
{
    std::map<char, int> mymap;

    mymap['b'] = 100;
    mymap['a'] = 200;
    mymap['c'] = 300;

    for (std::map<char, int>::iterator it = mymap.begin(); it != mymap.end(); it++) {
        std::cout << it->first << " => " << it->second << "\n";
    }

    return 0;
}

