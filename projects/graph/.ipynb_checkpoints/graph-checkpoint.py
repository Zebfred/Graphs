"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy



class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        #pass 
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        #pass
        self.vertices[v1].add(v2)  

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        #pass  
        return self.vertices[vertex_id]


    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #pass  
        #make a queue
        que = Queue()
        #enqueue the starting node
        que.enqueue(starting_vertex)

     #make a set to track if visited before
        visited = set()

     #while th queue isnt empty
        while que.size() > 0:
        # dequeue thing at the front of line, current_node
            current_node = que.dequeue()

     #unvisted node 
            if current_node not in visited:
            #mark if visited
                visited.add(current_node)
                print(current_node)
            
            #get neighbors of current_node
                neighbors = self.get_neighbors(current_node)
            # for each of the neighbors
                for neighbor in neighbors:
            # add to queue
                    que.enqueue(neighbor)


    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #pass  
        #make a stack
        sta = Stack()
        #push on starting node
        sta.push(starting_vertex)

        # set for track that been visited
        visited = set()
        # while stack isn't empty 
        while sta.size() > 0:
            #pop off top thing , current_node
            current_node = sta.pop()

        # if visit hasnt occured at this vertex
            if current_node not in visited:
                print(current_node)
                #mark visited
                visited.add(current_node)
                # get its neighbors
                neighbors = self.get_neighbors(current_node)
                # for each neighbors
                for neighbor in neighbors:
                    # add to stack
                    sta.push(neighbor)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        #pass  
        if visited == None:
            visited = set()


        if starting_vertex not in visited:
            visited.add(starting_vertex)
            print(starting_vertex)
            neighbors = self.get_neighbors(starting_vertex)

            for neighbor in neighbors:
                self.dft_recursive(neighbor, visited)


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        #pass  
        #make a queue
        que = Queue()
        #enqueue the starting node
        que.enqueue(starting_vertex)

     #make a set to track if visited before
        visited = set()

        #while th queue isnt empty
        while que.size() > 0:
            # dequeue thing at the front of line, current_node
            current_node = que.dequeue()

            #unvisted node 
            if current_node not in visited:
                #mark if visited
                visited.add(current_node)
                print(current_node)
                
                #get neighbors of current_node
                neighbors = self.get_neighbors(current_node)
                # for each of the neighbors
                for neighbor in neighbors:
                # add to queue
                        que.enqueue(neighbor)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        #pass
        sta = Stack()
        visited = set()
        sta.push([starting_vertex])

        while sta.size() > 0:
            current_path = sta.pop()
            if current_path[-1] not in visited:
                visited.add(current_path[-1])

            if current_path[-1] == destination_vertex:
                return current_path

            neighbors = self.get_neighbors(current_path[-1])
            for neighbor in neighbors:
                new_path = current_path + [neighbor]
                sta.push(new_path)  

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # #pass 
        # if visited == None:
        #     visited = set()

        # if path == None:
        #     path = [starting_vertex]

        # if starting_vertex not in visited:
        #     visited.add(starting_vertex)
        #     #path.append(starting_vertex)
        #     if starting_vertex == destination_vertex:
        #         return path
            
        #     neighbors = self.get_neighbors(starting_vertex)
        #     for neighbor in neighbors:
        #         ans = self.dfs_recursive(neighbor, destination_vertex, visited, path + [neighbor])
        #         if ans == None:
        #             continue
        #         return ans 

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
