#include <iostream>
#include <math.h>

using namespace std;

int main()
{
    int n = 13;
    cout << 2 * pow(2, ceil(log2(n))) - 1 << endl;    
    return 0;
}

