#include <stdio.h>
#include <stdlib.h>

typedef struct list {
    int item;
    struct list *next;
} list;

list *search_list(list *l, int x);

int main(void) {
    // Create root of linked list
    list root;
    list second;
    list third;
    list fourth;

    root.item = 1;
    second.item = 2;
    third.item = 3;
    fourth.item = 4;

    root.next = &second;
    second.next = &third;
    third.next = &fourth;

    // Search the list
    list *node = search_list(&root, 3);
    printf("%d\n", node->item); // 3

    // Search for an item not in the list
    list *node2 = search_list(&root, 5);
    if (node2 == NULL) {
        printf("%d not found\n", 5);
    } else {
        printf("%d\n", node2->item);
    }

    // Insertion into a List

    return 0;
}

// Recursive search
list *search_list(list *l, int x) {
    if (l == NULL) return NULL;
    if (l->item == x) return l;
    return search_list(l->next, x);
}

// Insert into linked list
void insert_list(list **l, int x) {
    list *p = (list *)malloc(sizeof(list));
    p->item = x;
    p->next = *l;
    *l = p;
}
