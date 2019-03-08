#include <iostream>

using namespace std;

int getsum(int bit[], int i)
{
    i++;
    int s = 0;
    while (i > 0) {
        s += bit[i];
        i -= i & (-i);
    }
    return s;
}


void update(int bit[], int n, int i, int v)
{
    i++;
    while (i <= n) {
        bit[i] += v;
        i += i & (-i);
    }
}

int *construct(int arr[], int n)
{
  int *bit = new int(n + 1);
  for (int i = 0; i <= n; i++) bit[i] = 0;
  for (int i = 0; i < n; i++) update(bit, n, i, arr[i]);
  return bit;
}

int main(void)
{
    int freq[] = {2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9};
    int n = sizeof(freq) / sizeof(freq[0]); 
    int *bit = construct(freq, n);
    cout << "Sum of elements in arr[0..5] is " << getsum(bit, 5) << endl;
    
    freq[3] += 6;
    update(bit, n, 3, 6);
    cout << "Sum of elements in arr[0..5] after update is " << getsum(bit, 5) << endl;

    return 0;
}

