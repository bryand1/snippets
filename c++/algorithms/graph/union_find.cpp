/*
 * Disjoint Set (Union-Find)
 * 
 * A disjoint-set is a data structure that keeps track of a set of elements
 * partitioned into a number of disjoint (non-overlapping) subsets. A union-find
 * algorithm performs two useful operations on such a data structure:
 * 
 * Union: Join two subsets into one subset.
 * 
 * Find: Determine which subset a particular element is in. This can be used for
 *       determining if two elements are in the same subset.
 *
 * 
 * https://www.geeksforgeeks.org/union-find/
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Edge
{
    int src, dest;
};

struct Graph
{
    // V: Number of vertices, E: Number of edges
    int V, E;
    // Graph is represented as an array of edges
    struct Edge* edge;
};

struct Graph* create_graph(int V, int E)
{
    struct Graph* graph = (struct Graph*) malloc(sizeof(struct Graph));
    graph->V = V;
    graph->E = E;

    graph->edge = (struct Edge*) malloc(graph->E * sizeof(struct Edge));

    return graph;
}

int find(int parent[], int i)
{
    if (parent[i] == -1) {
        return i;
    }
    return find(parent, parent[i]);
}

void Union(int parent[], int x, int y)
{
    int xset = find(parent, x);
    int yset = find(parent, y);
    if (xset != yset) {
        parent[xset] = yset;
    }
}

// Check whether a graph contains a cycle or not
int is_cycle(struct Graph* graph)
{
    int *parent = (int *) malloc(graph->V * sizeof(int));

    // Initialize all subsets as single element sets
    memset(parent, -1, graph->V * sizeof(int));

    // Iterate through all edges of graph, find subset of both
    // vertices of every edge. If both subsets are the same, then
    // there is a cycle in graph.
    for (int i = 0; i < graph->E; i++) {
        int x = find(parent, graph->edge[i].src);
        int y = find(parent, graph->edge[i].dest);
        if (x == y) {
            return 1;
        }
        Union(parent, x, y);
    }
    return 0;
}

int main()
{
    /* Let us create the following graph 
         0 
        |  \ 
        |    \ 
        1-----2 */     
    int V = 3, E = 3; 
    struct Graph* graph = create_graph(V, E); 
  
    // edge 0->1 
    graph->edge[0].src = 0; 
    graph->edge[0].dest = 1; 
  
    // edge 1->2 
    graph->edge[1].src = 1; 
    graph->edge[1].dest = 2; 
  
    // edge 0->2 
    graph->edge[2].src = 0; 
    graph->edge[2].dest = 2;

    if (is_cycle(graph)) {
        printf("Graph contains cycle\n");
    } else {
        printf("Graph does not contain cycle\n"); 
    }

    return 0; 
}
