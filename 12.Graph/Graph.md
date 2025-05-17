# 📊 Graph Data Structure

## 📌 Introduction

A **Graph** is a non-linear data structure that consists of:

* **Vertices (Nodes)** – Represent entities or objects
* **Edges** – Represent relationships or connections between vertices

Mathematically, a graph **G** is defined as:

```
G = (V, E)
```

Where:
* `V` is a set of vertices
* `E` is a set of edges connecting the vertices

```mermaid
graph LR
    A((A)) --- B((B))
    B --- C((C))
    A --- C
    D((D)) --- E((E))
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bfb,stroke:#333,stroke-width:2px
    style D fill:#fbb,stroke:#333,stroke-width:2px
    style E fill:#fbf,stroke:#333,stroke-width:2px
```

## 📋 Types of Graphs

### 1. Directed Graph (Digraph)

* Edges have direction
* Represented as ordered pairs `(u, v)` indicating edge from `u` to `v`
* Example: Social media followers (A follows B)

```mermaid
graph LR
    A((A)) --> B((B))
    B --> C((C))
    C --> A
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bfb,stroke:#333,stroke-width:2px
```

### 2. Undirected Graph

* Edges have no direction
* Represented as unordered pairs `{u, v}`
* Example: Facebook friendship (A and B are friends)

```mermaid
graph LR
    A((A)) --- B((B))
    B --- C((C))
    C --- A
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bfb,stroke:#333,stroke-width:2px
```

### 3. Weighted Graph

* Each edge has a weight or cost associated with it
* Example: Map with distances between cities

```mermaid
graph LR
    A((A)) -- 5 --> B((B))
    B -- 3 --> C((C))
    C -- 4 --> A
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bfb,stroke:#333,stroke-width:2px
```

### 4. Unweighted Graph

* No weights on the edges
* Simple connections between vertices

### 5. Cyclic Graph

* Contains at least one cycle (a path that starts and ends at the same vertex)
* Example: Circular dependencies in tasks

```mermaid
graph LR
    A((A)) --> B((B))
    B --> C((C))
    C --> A
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bfb,stroke:#333,stroke-width:2px
```

### 6. Acyclic Graph

* No cycles present
* Example: Hierarchical file system

```mermaid
graph TD
    A((Root)) --> B((Folder 1))
    A --> C((Folder 2))
    B --> D((File 1))
    B --> E((File 2))
    C --> F((File 3))
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bfb,stroke:#333,stroke-width:2px
```

### 7. Connected Graph

* There is a path between every pair of vertices
* All vertices are reachable from any other vertex

### 8. Disconnected Graph

* At least one pair of vertices has no path between them
* Contains multiple components

```mermaid
graph LR
    A((A)) --- B((B))
    B --- C((C))
    D((D)) --- E((E))
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bfb,stroke:#333,stroke-width:2px
    style D fill:#fbb,stroke:#333,stroke-width:2px
    style E fill:#fbf,stroke:#333,stroke-width:2px
```

### 9. Complete Graph

* Every vertex is connected to every other vertex
* For `n` vertices, total edges = `n(n-1)/2` in undirected graph

```mermaid
graph LR
    A((A)) --- B((B))
    A --- C((C))
    A --- D((D))
    B --- C
    B --- D
    C --- D
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bfb,stroke:#333,stroke-width:2px
    style D fill:#fbb,stroke:#333,stroke-width:2px
```

### 10. Sparse and Dense Graphs

* **Sparse**: Few edges compared to number of vertices
* **Dense**: Number of edges is close to the maximum possible

### 11. Tree

* A special kind of graph that is connected and acyclic
* For `n` nodes, it has exactly `n-1` edges

```mermaid
graph TD
    A((Root)) --> B((Child 1))
    A --> C((Child 2))
    B --> D((Leaf 1))
    B --> E((Leaf 2))
    C --> F((Leaf 3))
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
    style C fill:#bfb,stroke:#333,stroke-width:2px
```

### 12. Subgraph

* A graph formed from a subset of the vertices and edges of another graph

### 13. Multigraph

* Multiple edges (parallel edges) between the same pair of vertices

```mermaid
graph LR
    A((A)) -- Edge 1 --> B((B))
    A -- Edge 2 --> B
    style A fill:#f9f,stroke:#333,stroke-width:2px
    style B fill:#bbf,stroke:#333,stroke-width:2px
```

### 14. Graph Representation

#### Adjacency Matrix
* 2D matrix of size V×V
* `matrix[i][j] = 1` if there is an edge from vertex i to j
* `matrix[i][j] = 0` otherwise

#### Adjacency List
* Array of lists
* Each list contains the neighbors of a vertex
* More space-efficient for sparse graphs

## 💡 Use Cases

* **Social Networks**: Friend connections, follower relationships
* **Web Page Linking**: Google PageRank algorithm
* **Network Routing**: Dijkstra's, Bellman-Ford algorithms
* **Scheduling**: Task dependencies and project management
* **Game Development**: Maps and AI pathfinding
* **GPS Navigation**: Finding shortest paths
* **Circuit Design**: Electronic circuit connections
* **Dependency Resolution**: Package managers, build systems

---

*Note: All diagrams are interactive in supported Markdown viewers*

