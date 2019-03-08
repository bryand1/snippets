#include <iostream>

using namespace std;

void insertion_sort(int arr[], int n)
{
    for (int i = 1; i < n; i++) {
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && key < arr[j]) {
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}

void print_arr(int arr[], int n)
{
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main()
{
    int freq[] {2, 2, 4, 5, 6, 1, 0, 9, 10, 11, 12};
    int n = sizeof(freq) / sizeof(freq[0]);
    insertion_sort(freq, n);
    print_arr(freq, n);
}

