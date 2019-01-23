#include <stdio.h>
#include <stdlib.h>

struct Node {
  void *data;
  struct Node *next;
};

void push(struct Node **head_ref, void *new_data, size_t data_size) {
    struct Node *new_node = (struct Node *)malloc(sizeof(struct Node));
    new_node->data = malloc(data_size);
    new_node->next = (*head_ref);
    for (int i = 0; i < data_size; i++) {
        *(char *)(new_node->data + i) = *(char *)(new_data + i); 
    }
    // Change head pointer as new node added at the beginning
    (*head_ref) = new_node;
}

void print_list(struct Node *node, void (*fptr)(void *)) {
    while (node != NULL) {
        (*fptr)(node->data);
        node = node->next;
    }
}

// Print integer
void print_int(void *n) {
    printf(" %d", *(int *)n);
}

// Print floating point number
void print_float(void *f) {
    printf(" %f", *(float *)f);
}

// Driver to test functions
int main(void) {
    struct Node *start = NULL;

    // Create and print a linked list of integers
    size_t int_size = sizeof(int);
    int arr[] = {10, 20, 30, 40, 50};
    int i;
    for (i = 4; i >= 0; i--) {
        push(&start, &arr[i], int_size);
    }
    printf("Created integer linked list is: ");
    print_list(start, print_int);
    printf("\n");
    return 0;
}
