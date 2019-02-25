/*
 * Initialize std::vector in multiple ways
 *
 * 1) Empty vector of size n
 * 2) Vector of size n with each value set to 2
 * 3) Copy of Vector #2
 * 4) Initialization shorthand
 */
#include <bits/stdc++.h>

using namespace std;

void print_vector(vector<int>& v) {
    for (int x : v) {
        cout << x << " ";
    }
    cout << endl;
}

int main(void) {
    int n = 10;
    vector<int> v1(n);
    vector<int> v2(n, 2);
    vector<int> v3(v2.begin(), v2.end());
    vector<int> v4{20, 20, 20, 20, 20};

    print_vector(v1);
    print_vector(v2);
    print_vector(v3);
    print_vector(v4);
}
