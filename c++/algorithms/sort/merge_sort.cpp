#include <iostream>

void merge(int A[], int lo, int mid, int hi)
{
    int n1 = mid - lo + 1;
    int n2 = hi - mid;
    int L[n1];
    int R[n2];
    int i, j, k;
    for (i = 0; i < n1; i++) {
        L[i] = A[lo + i];
    }
    for (j = 0; j < n2; j++) {
        R[j] = A[mid + 1 + j];
    }
    i = j = 0;
    k = lo;
    while (i < n1 && j < n2) {
        if (L[i] < R[j]) {
            A[k] = L[i];
            i++;
        } else {
            A[k] = R[j];
            j++;
        }
        k++;
    }
    while (i < n1) {
        A[k] = L[i];
        i++;
        k++;
    }
    while (j < n2) {
        A[k] = R[j];
        j++;
        k++;
    }
}

void merge_sort(int A[], int lo, int hi)
{
    if (lo < hi) {
        int mid = lo + (hi - lo) / 2;
        merge_sort(A, lo, mid);
        merge_sort(A, mid + 1, hi);
        merge(A, lo, mid, hi);
    }
}

void print_arr(int A[], int n)
{
    for (int i = 0; i < n; i++) {
        std::cout << A[i] << " ";
    }
    std::cout << std::endl;
}

int main()
{
    int freq[] {2, 4, 9, 10, 0, 2, 7, 8, 18, 2002};
    int n = sizeof(freq) / sizeof(freq[0]);
    merge_sort(freq, 0, n - 1);
    print_arr(freq, n);
    return 0;
}

