#include <iostream>
#include <assert.h>

using namespace std;

int binary_search(int A[], int n, int x)
{
    int l = 0, r = n - 1;
    while (l <= r) {
        int m = l + (r - l) / 2;
        if (A[m] == x) {
            return m;
        } else if (A[m] > x) {
            r = m - 1;
        } else {
            l = m + 1;
        }
    }
    return - 1;
}

int main(void)
{
    int A[] {1, 3, 7, 9, 10};
    int n = sizeof(A) / sizeof(A[0]);
    cout << binary_search(A, n, 1) << endl;
    cout << binary_search(A, n, 10) << endl;
    cout << binary_search(A, n, 7) << endl;
    cout << binary_search(A, n, 1000) << endl;
    return 0;
}

