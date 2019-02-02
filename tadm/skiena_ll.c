#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

typedef int item_type;

void print_item(item_type x) {
    printf("item %d\n", x);
}

typedef struct list {
    item_type item;
    struct list *next;
} list;

list *search_list(list *l, item_type x) {
    if (l == NULL) return NULL;
    if (l->item == x) return l;
    return search_list(l->next, x);
}

int insert_list(list **l, item_type x) {
    list *p;
    p = malloc(sizeof(list));
    if (!p) return -1;
    p->item = x;
    p->next = *l;
    *l = p;
    return 0;
}

list *predecessor_list(list *l, item_type x) {
    if ((l == NULL) || (l->next == NULL)) return NULL;
    if ((l->next)->item == x) return l;
    return predecessor_list(l->next, x);
}

int delete_list(list **l, item_type x) {
    list *p;
    list *pred;

    p = search_list(*l, x);
    if (p == NULL) return -1;

    pred = predecessor_list(*l, x);
    if (pred == NULL) {
        *l = p->next;  // delete node at head of linked list
    } else {
        pred->next = p->next;
    }

    free(p);

    return 0;
}

void free_list(list **l) {
  item_type x;
  while (1) {
    if (*l == NULL) break;
    x = (*l)->item;
    if (delete_list(l, (*l)->item) < 0) {
        printf("Failed to delete item %d\n", x);
    }
  }
}

void print_list(list *l) {
    if (!l) return;
    print_item(l->item);
    return print_list(l->next);
}

list *head;

int main(void) {
    for (int i = 0; i < 100; i++) {
        insert_list(&head, i);
    }
    print_list(head);

    free_list(&head);
    return 0;
}

