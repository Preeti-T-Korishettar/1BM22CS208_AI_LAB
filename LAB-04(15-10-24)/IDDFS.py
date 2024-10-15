from collections import defaultdict

# This class represents a directed graph using adjacency list representation
class Graph:
    def __init__(self):
        # Initialize an empty default dictionary to store the graph
        self.graph = defaultdict(list)

    # Function to add an edge to the graph
    def add_edge(self, u, v):
        self.graph[u].append(v)

    # A function to perform a Depth-Limited search from given source 'src'
    def DLS(self, src, target, max_depth, visited):
        if src == target:
            return True

        if max_depth <= 0:
            return False

        # Mark the current node as visited
        visited.add(src)

        # Recur for all the vertices adjacent to this vertex
        for neighbor in self.graph[src]:
            if neighbor not in visited:
                found = self.DLS(neighbor, target, max_depth - 1, visited)
                if found:
                    return True

        # Remove the node from visited for other paths
        visited.remove(src)
        return False

    # IDDFS to search if target is reachable from src within max_depth
    def IDDFS(self, src, target, max_depth):
        for depth in range(max_depth + 1):
            visited = set()
            found = self.DLS(src, target, depth, visited)
            if found:
                return True
        return False

def read_graph():
    graph = Graph()

    # Input the number of vertices
    while True:
        try:
            num_vertices = int(input("Enter the number of vertices: "))
            if num_vertices <= 0:
                print("Number of vertices must be a positive integer. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer value.")

    # Input the vertices (characters)
    vertices = []
    print("Enter the vertices (single characters). Example: A B C D")
    while True:
        input_vertices = input(f"Enter {num_vertices} unique characters separated by spaces: ").strip().split()
        if len(input_vertices) != num_vertices:
            print(f"Please enter exactly {num_vertices} unique characters.")
            continue
        if len(set(input_vertices)) != num_vertices:
            print("Duplicate characters detected. Please enter unique characters.")
            continue
        vertices = input_vertices
        break

    print("\nVertices in the graph:", ' '.join(vertices))

    # Input the number of edges
    while True:
        try:
            num_edges = int(input("\nEnter the number of edges: "))
            if num_edges < 0:
                print("Number of edges cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer value.")

    # Input the edges
    print("\nEnter each edge as two characters separated by a space (e.g., A B for A -> B):")
    for i in range(num_edges):
        while True:
            edge_input = input(f"Enter edge {i + 1}: ").strip().split()
            if len(edge_input) != 2:
                print("Each edge must consist of exactly two characters. Please try again.")
                continue
            u, v = edge_input
            if u not in vertices or v not in vertices:
                print("Both vertices must be among the previously entered vertices. Please try again.")
                continue
            graph.add_edge(u, v)
            break

    return graph, vertices

def main():
    print("### Iterative Deepening Depth-First Search (IDDFS) ###\n")
    graph, vertices = read_graph()

    # Input source node
    while True:
        src = input("\nEnter the source node: ").strip()
        if src not in vertices:
            print("Source node must be one of the vertices in the graph. Please try again.")
            continue
        break

    # Input target node
    while True:
        target = input("Enter the target node: ").strip()
        if target not in vertices:
            print("Target node must be one of the vertices in the graph. Please try again.")
            continue
        break

    # Input maximum depth
    while True:
        try:
            max_depth = int(input("Enter the maximum depth: "))
            if max_depth < 0:
                print("Maximum depth cannot be negative. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer value.")

    # Perform IDDFS
    print(f"\nSearching for target '{target}' from source '{src}' with maximum depth {max_depth}...\n")
    if graph.IDDFS(src, target, max_depth):
        print(f"Target '{target}' is reachable from source '{src}' within max depth {max_depth}.")
    else:
        print(f"Target '{target}' is NOT reachable from source '{src}' within max depth {max_depth}.")

if __name__ == "__main__":
    main()
