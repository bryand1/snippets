#include <iostream>

void swap(int arr[], int a, int b)
{
   int temp = arr[a];
   arr[a] = arr[b];
   arr[b] = temp;
}

void bubble_sort(int arr[], int n)
{
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr, j, j + 1);
            }
        }
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
    bubble_sort(freq, n);
    print_arr(freq, n);
    return 0;
}

