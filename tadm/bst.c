#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

typedef int item_type;

void print_item(item_type x) {
    printf("item %d\n", x);
}

typedef struct tree {
    item_type item;
    struct tree *parent;
    struct tree *left;
    struct tree *right;
} tree;

tree *find_minimum(tree *t) {
    if (!t) return NULL;
    while (t->left) t = t->left;
    return t;
}

tree *find_maximum(tree *t) {
    if (!t) return NULL;
    while (t->right) t = t->right;
    return t;
}

void inorder_traverse(tree *t) {
    if (!t) return;
    inorder_traverse(t->left);
    print_item(t->item);
    inorder_traverse(t->right);
}

void preorder_traverse(tree *t) {
    if (!t) return;
    print_item(t->item);
    preorder_traverse(t->left);
    preorder_traverse(t->right);
}

void postorder_traverse(tree *t) {
    if (!t) return;
    postorder_traverse(t->left);
    postorder_traverse(t->right);
    print_item(t->item);
}

tree *get_node(void) {
    tree *n;
    n = malloc(sizeof(*n));
    if (!n) return NULL;
    n->parent = NULL;
    n->left = NULL;
    n->right = NULL;
    n->item = 0;
    return n;
}

int insert_list(tree **r, item_type x, tree *parent) {
    tree *n;
    if (!*r) {
        n = get_node();
        if (!n) return -1;
        n->item = x;
        n->parent = parent;
        *r = n;
        return 0;
    }
    if ((*r)->item < x) {
        return insert_list(&(*r)->right, x, *r);
    } else {
        return insert_list(&(*r)->left, x, *r);
    }
}
