#include <stdio.h>
#include <string.h>
#include "editdistance.h"
#include "bool.h"

cell m[MAXLEN+1][MAXLEN+1];

void row_init(int i) {
    m[0][i].cost = i;
    if (i > 0)
        m[0][i].parent = INSERT;
    else
        m[0][i].parent = -1;
}

void column_init(int i) {
    m[i][0].cost = i;
    if (i > 0)
        m[i][0].parent = DELETE;
    else
        m[i][0].parent = -1;
}

int match(char c, char d) {
    if (c == d) return 0;
    else return 1;
}

int indel(char c) {
    return 1;
}

void goal_cell(char *s, char *t, int *i, int *j) {
    *i = strlen(s) - 1;
    *j = strlen(t) - 1;
}

void insert_out(char *t, int j) {
    printf("I");
}

void delete_out(char *s, int i) {
    printf("D");
}

void match_out(char *s, char *t, int i, int j) {
    if (s[i] == t[j]) printf("M");
    else printf("S");
}

int string_compare(char *s, char *t) {
    int i, j, k;  // counters
    int opt[3];   // cost of the three options

    for (i = 0; i < MAXLEN; i++) {
        row_init(i);
        column_init(i);
    }
    for (i = 1; i < strlen(s); i++) {
        for (j = 1; j < strlen(t); j++) {
            opt[MATCH] = m[i-1][j-1].cost + match(s[i], t[j]);
            opt[INSERT] = m[i][j-1].cost + indel(t[j]);
            opt[DELETE] = m[i-1][j].cost + indel(s[i]);

            m[i][j].cost = opt[MATCH];
            m[i][j].parent = MATCH;
            for (k = INSERT; k <= DELETE; k++) {
                if (opt[k] < m[i][j].cost) {
                    m[i][j].cost = opt[k];
                    m[i][j].parent = k;
                }
            }
        }
    }
    goal_cell(s, t, &i, &j);
    return m[i][j].cost;
}

void reconstruct_path(char *s, char *t, int i, int j) {
    if (m[i][j].parent == -1) return;
    if (m[i][j].parent == MATCH) {
        reconstruct_path(s, t, i - 1, j - 1);
        match_out(s, t, i, j);
        return;
    }
    if (m[i][j].parent == INSERT) {
        reconstruct_path(s, t, i, j - 1);
        insert_out(t, j);
        return;
    }
    if (m[i][j].parent == DELETE) {
        reconstruct_path(s, t, i - 1, j);
        delete_out(s, i);
        return;
    }
}

void print_matrix(char *s, char *t, bool costQ) {
	int i,j;			/* counters */
	int x,y;			/* string lengths */

	x = strlen(s);
	y = strlen(t);

	printf("   ");
	for (i=0; i<y; i++)
		printf("  %c",t[i]);
	printf("\n");

	for (i=0; i<x; i++) {
		printf("%c: ",s[i]);
		for (j=0; j<y; j++) {
			if (costQ == TRUE)
				printf(" %2d",m[i][j].cost);
			else
				printf(" %2d",m[i][j].parent);

		}
		printf("\n");
	}
}

int main(void) {
    // char *a = "abcd";
    // char *b = "xbdd";
    // printf("%d\n", string_compare(a, b));  // 2
    char *a = "thou-shalt-not";
    char *b = "you-should-not";
    printf("%d\n", string_compare(a, b));
    reconstruct_path(a, b, strlen(a) - 1, strlen(b) - 1);
    printf("\n");
    print_matrix(a, b, TRUE);
    return 0;
}
