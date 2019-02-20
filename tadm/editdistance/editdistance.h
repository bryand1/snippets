#define MAXLEN 101

#define MATCH 0
#define INSERT 1
#define DELETE 2

typedef struct {
    int cost;
    int parent;
} cell;
