#include <bits/stdc++.h>

using namespace std;

int getsum(vector<int>& ft, int i) {
    i++;
    int s = 0;
    while (i > 0) {
        s += ft[i];
        i -= i & (-i);
    }
    return s;
}

void update(vector<int>& ft, int n, int i, int v) {
    i++;
    while (i <= n) {
        ft[i] += v;
        i += i & (-i);
    }
}

vector<int> construct(vector<int>& v) {
    int n = (int)v.size();
    vector<int> ft(n + 1);
    for (int i = 0; i < n; i++) update(ft, n, i, v[i]);
    return ft;
}

int main(void) {
    vector<int> a{2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4};
    vector<int> b = construct(a);
    cout << getsum(b, 7) << endl;  // 20
    return 0;
}
