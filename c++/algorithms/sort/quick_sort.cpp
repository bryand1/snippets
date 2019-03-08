#include <iostream>

void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

void print_arr(int arr[], int n)
{
    for (int i = 0; i < n; i++) {
        std::cout << arr[i] << " ";
    }
    std::cout << std::endl;
}

int partition(int arr[], int lo, int hi)
{
    int pivot = arr[hi];
    int i = lo - 1;
    for (int j = lo; j < hi; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[hi]);
    return i + 1;
}

void quick_sort(int arr[], int lo, int hi)
{
    if (lo < hi) {
        int pivot = partition(arr, lo, hi);
        quick_sort(arr, lo, pivot - 1);
        quick_sort(arr, pivot + 1, hi);
    }
}

int main()
{
    int freq[] {2, 1, 0, 3, 4, 5, 19, 20, 27, 9};
    int n = sizeof(freq) / sizeof(freq[0]);
    quick_sort(freq, 0, n - 1);
    print_arr(freq, n);
    return 0;
}

