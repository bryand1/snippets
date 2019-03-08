#include <iostream>
#include <math.h>

using namespace std;

// Determine the height of a segment tree
// from array with n values
int main()
{
    int nodes = 13;
    cout << ceil(log2((float)nodes)) + 1.0 << endl;
    return 0;
}

