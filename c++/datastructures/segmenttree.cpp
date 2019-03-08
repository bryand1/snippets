#include <iostream>
#include <assert.h>
#include <math.h>

#define MAX_VALUE 2100000

using namespace std;

int minquery(int segtree[], int qlo, int qhi, int lo, int hi, int pos)
{
    if (qlo <= lo && qhi >= hi) {
        return segtree[pos];
    }
    if (qlo > hi || qhi < lo) {
        return MAX_VALUE;
    }
    int mid = lo + (hi - lo) / 2;
    return min(
        minquery(segtree, qlo, qhi, lo, mid, 2 * pos + 1),
        minquery(segtree, qlo, qhi, mid + 1, hi, 2 * pos + 2));
}

void construct(int input[], int segtree[], int lo, int hi, int pos)
{
    if (lo == hi) {
        segtree[pos] = input[lo];
        return;
    }
    int mid = lo + (hi - lo) / 2;
    construct(input, segtree, lo, mid, 2 * pos + 1);
    construct(input, segtree, mid + 1, hi, 2 * pos + 2);
    segtree[pos] = min(segtree[2 * pos + 1], segtree[2 * pos + 2]);
}

int main()
{
    int freq[] {2, 4, 5, 2, 1, 9, 10, 7, 6, 2};
    int n = sizeof(freq) / sizeof(freq[0]);
    int size = 2 * (int)pow(2, ceil(log2(n))) - 1;
    int segtree[size];
    construct(freq, segtree, 0, n - 1, 0);    
    cout << minquery(segtree, 0, 5, 0, n - 1, 0) << endl;
    return 0;
}

