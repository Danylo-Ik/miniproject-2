import unittest

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
    graph=to_edge_dict(get_graph_from_file(filename))
    with open(filename.split('.')[0]+'.dot',mode='w',encoding='utf-8') as file:
        file.write('digraph {\n')
        dict_values=list(graph.values())
        dict_keys=list(graph.keys())
        dict_keys_len=len(dict_keys)
        for i in range(dict_keys_len):
            for j in range(len(dict_values[i])):
                file.write(f'{dict_keys[i]} -> {dict_values[i][j]}\n')
        file.write('}')


class GraphFunctionsTest(unittest.TestCase):

    def test_get_graph_from_file_empty(self):
        # Test with an empty file
        with open("empty.txt", "w") as f:
            f.write("")
        graph = get_graph_from_file("empty.txt")
        self.assertEqual(graph, [])

    def test_get_graph_from_file_single_line(self):
        # Test with a single line
        with open("single_line.txt", "w") as f:
            f.write("1,2\n")
        graph = get_graph_from_file("single_line.txt")
        self.assertEqual(graph, [[1, 2]])

    def test_get_graph_from_file_multiple_lines(self):
        # Test with multiple lines
        with open("multiple_lines.txt", "w") as f:
            f.write("1,2\n")
            f.write("3,4\n")
            f.write("1,5\n")
        graph = get_graph_from_file("multiple_lines.txt")
        self.assertEqual(graph, [[1, 2], [3, 4], [1, 5]])

    def test_get_graph_from_file_invalid_format(self):
        # Test with invalid format (missing comma)
        with open("invalid_format.txt", "w") as f:
            f.write("1 2\n")
        with self.assertRaises(ValueError):
            get_graph_from_file("invalid_format.txt")

    def test_to_edge_dict_empty_list(self):
        # Test with an empty list
        edge_dict = to_edge_dict([])
        self.assertEqual(edge_dict, {})

    def test_to_edge_dict_simple_list(self):
        # Test with a simple list
        edge_list = [[1, 2], [3, 4]]
        edge_dict = to_edge_dict(edge_list)
        self.assertEqual(edge_dict, {1: [2], 2: [1], 3: [4], 4: [3]})

    # Add more tests for to_edge_dict with different scenarios

    def test_is_edge_in_graph_existing_edge(self):
        # Test with an existing edge
        graph = {1: [2, 3], 4: [5]}
        edge = [1, 2]
        self.assertTrue(is_edge_in_graph(graph, edge))

    def test_is_edge_in_graph_nonexistent_edge(self):
        # Test with a nonexistent edge
        graph = {1: [2, 3], 4: [5]}
        edge = [3, 4]
        self.assertFalse(is_edge_in_graph(graph, edge))

    # Add more tests for is_edge_in_graph with different scenarios

    def test_add_edge_existing_edge(self):
        # Test adding an existing edge
        graph = {1: [2]}
        edge = [1, 2]
        updated_graph = add_edge(graph.copy(), edge)
        self.assertEqual(updated_graph, graph)

    def test_add_edge_new_edge(self):
        # Test adding a new edge
        graph = {1: [2]}
        edge = [3, 4]
        updated_graph = add_edge(graph.copy(), edge)
        self
