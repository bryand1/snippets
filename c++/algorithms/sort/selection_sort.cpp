#include <iostream>

void swap(int arr[], int a, int b)
{
   int temp = arr[a];
   arr[a] = arr[b];
   arr[b] = temp;
}

void selection_sort(int arr[], int n)
{
    int i, j, m;
    for (i = 0; i < n; i++) {
        m = i;
        for (j = i; j < n; j++) {
            if (arr[j] < arr[m]) {
                m = j;
            }
        }
        swap(arr, i, m);
    }
}

void print_arr(int arr[], int n)
{
    for (int i = 0; i < n; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

int main()
{
    int freq[] {2, 4, 6, 8, 10, 1, 2, 3, 10, 100};
    int n = sizeof(freq) / sizeof(freq[0]);
    selection_sort(freq, n);
    print_arr(freq, n);
    return 0;
}

