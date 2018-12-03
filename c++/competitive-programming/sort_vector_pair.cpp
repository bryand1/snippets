#include <bits/stdc++.h>

using namespace std;

int main() {
    vector<pair<int, int>> v;
    v.push_back({1, 2});
    v.push_back({2, 3});
    v.push_back({1, 5});
    sort(v.begin(), v.end());
    cout << v[1].first << endl;

    return 0;
}
