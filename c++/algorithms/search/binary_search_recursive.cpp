#include <iostream>
#include <assert.h>

using namespace std;

// Recursive implementation
int binary_search(int A[], int l, int r, int x)
{
    if (l <= r) {
        int m = l + (r - l) / 2;
        if (A[m] == x) {
            return m;
        } else if (A[m] > x) {
            return binary_search(A, l, m - 1, x);
        } else {
            return binary_search(A, l + 1, r, x);
        }
    } else {
        return -1;
    }
}

int main(void)
{
    int A[10] = {1, 3, 5, 9, 10, 100, 200, 300, 333, 400};
    int lo = 0;
    int hi = 9;
    cout << binary_search(A, lo, hi, 5) << endl;
    cout << binary_search(A, lo, hi, 1) << endl;    // First item
    cout << binary_search(A, lo, hi, 400) << endl;  // Last item
    cout << binary_search(A, lo, hi, 666) << endl; // Missing item
    assert(binary_search(A, lo, hi, 7) == -1);
    return 0;
}

