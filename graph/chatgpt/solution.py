"""
This module contains functions to work with graphs:
get_graph_from_file() - read graph edges from txt file and save them as lists
to_edge_dict() - present the graph as a dictionary with nodes as keys and edges as values
is_edge_in_graph() - return True if given edge is in graph or False otherwise
add_edge() - add a new edge to graph
del_edge() - delete an edge from graph
add_node() - add a new node to graph
del_node() - delete a node from graph
convert_to_dot() - read graph from txt file and write a representation into DOT file
"""
def get_graph_from_file(file_name: str) -> list:
    """ 
    (str) -> (list)
    
    Read graph from file and return a list of edges.
    
    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """
    with open(file_name, 'r', encoding='utf-8') as file:
        edge_list = [[int(el) for el in line.strip("\n").split(",")] for line in file]
    return edge_list

def to_edge_dict(edge_list: list) -> dict:
    """ 
    (list) -> (dict)

    Convert a graph from list of edges to dictionary of vertices.
    
    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
    graph = {}
    for pair in edge_list:
        for el in pair:
            if el not in graph:
                graph[el] = []
            graph[el].extend([n for n in pair if n != el])
    for key in graph:
        graph[key] = sorted(graph[key])
    return graph

def is_edge_in_graph(graph: dict, edge: tuple) -> bool:
    """ 
    (dict, tuple) -> bool
    
    Return True if graph contains a given edge and False otherwise.
    
    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """
    edge = list(edge)
    for key in graph:
        for el in graph[key]:
            if edge in ([key, el], [el, key]):
                return True
            continue
    return False

def add_edge(graph: dict, edge: tuple) -> dict:
    """ 
    (dict, tuple) -> dict
    
    Add a new edge to the graph and return new graph. 
    
    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (1, 3))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    edge = list(edge)
    if is_edge_in_graph(graph, edge):
        return graph
    for el in edge:
        if el in graph:
            graph[el].extend(n for n in edge if n != el)
        else:
            graph[el] = [n for n in edge if n != el]
    return graph

def del_edge(graph: dict, edge: tuple) -> dict:
    """ 
    (dict, tuple) -> (dict)
    
    Delete an edge from the graph and return a new graph.
    
    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    edge = list(edge)
    if not is_edge_in_graph(graph, edge):
        return graph
    for el in edge:
        if el in graph:
            for i in [n for n in edge if n != el]:
                graph[el].remove(i)
    return graph

def add_node(graph: dict, node: int) -> dict:
    """ 
    (dict, int) -> (dict)
    
    Add a new node to the graph and return a new graph.
    
    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    if node in graph:
        return graph
    graph[node] = []
    return graph

def del_node(graph: dict, node: int) -> dict:
    """ 
    (dict, int) -> (dict)
    
    Delete a node and all incident edges from the graph.
    
    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    if node not in graph:
        return graph
    connected_nodes = graph.pop(node)
    for el in connected_nodes:
        graph[el].remove(node)
    return graph
def sort_by_first_el(edges: list) -> int:
    """
    Key function to sort graphs edges by first node
    """
    return edges[0]

def convert_to_dot(filename: str) -> None:
    """
    Get graph from a file and save the directed graph to a file in a dot format with the same name.
    >>> convert_to_dot('data1.txt')
    >>> with open("data1.dot", "r", encoding = "utf-8") as result:
    ...     file_text = result.read()
    ...     print(file_text)
    data1.txt digraph {
    1 -> 2
    1 -> 5
    3 -> 4
    }
    """
    graph_str = ""
    graph_edges = sorted(get_graph_from_file(filename), key=sort_by_first_el)
    for [x, y] in graph_edges:
        graph_str += str(x) + " -> " + str(y)
        graph_str += '\n'
    extension_lst = filename.split(".")
    extension_lst.pop()
    extension_lst.append("dot")
    new_filename = ".".join(extension_lst)
    with open(new_filename, 'w', encoding='utf-8') as file:
        file.write(filename)
        file.write(" ")
        file.write('digraph {')
        file.write('\n')
        file.write(graph_str)
        file.write('}')
