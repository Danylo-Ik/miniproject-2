import unittest
from solution import *
import os

class TestGraphFunctions(unittest.TestCase):

    # Test cases for get_graph_from_file
    def test_get_graph_from_file(self):
        # Test reading data from file and returning correct graph edges
        expected_edges = [[1, 2], [3, 4], [1, 5]]
        self.assertEqual(get_graph_from_file("/Users/danyilikonnikov/Desktop/Projects/Sem_2/Miniproject_2/miniproject-2/graph/data1.txt"), expected_edges)

    # Test cases for to_edge_dict
    def test_to_edge_dict(self):
        # Test converting graph edges list to dictionary
        edge_list = [[1, 2], [3, 4], [1, 5]]
        expected_dict = {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
        self.assertEqual(to_edge_dict(edge_list), expected_dict)

    # Test cases for is_edge_in_graph
    def test_is_edge_in_graph(self):
        # Test checking if edge exists in graph
        graph = {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
        edge = [1, 2]
        self.assertTrue(is_edge_in_graph(graph, edge))

        # Add more test cases for edge not in graph and edge with missing vertex

    # Test cases for add_edge
    def test_add_edge(self):
        # Test adding a new edge to the graph
        graph = {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
        new_edge = [1, 3]
        expected_graph = {1: [2, 5, 3], 2: [1], 3: [4, 1], 4: [3], 5: [1]}
        self.assertEqual(add_edge(graph, new_edge), expected_graph)

        # Add more test cases for adding existing edge, adding edge with missing vertex, etc.

    # Test cases for del_edge
    def test_del_edge(self):
        # Test removing an existing edge from the graph
        graph = {1: [2, 5, 3], 2: [1], 3: [4, 1], 4: [3], 5: [1]}
        edge_to_delete = [1, 3]
        expected_graph = {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
        self.assertEqual(del_edge(graph, edge_to_delete), expected_graph)

        # Test removing a non-existent edge from the graph
        non_existent_edge = [2, 3]
        self.assertEqual(del_edge(graph, non_existent_edge), graph)

    # Test cases for add_node
    def test_add_node(self):
        # Test adding a new node to the graph
        graph = {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
        new_node = 6
        expected_graph = {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1], 6: []}
        self.assertEqual(add_node(graph, new_node), expected_graph)

        # Add more test cases for adding existing node, etc.

    # Test cases for del_node
    def test_del_node(self):
        # Test removing a node from the graph
        graph = {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
        node_to_delete = 5
        expected_graph = {1: [2], 2: [1], 3: [4], 4: [3]}
        self.assertEqual(del_node(graph, node_to_delete), expected_graph)

        # Add more test cases for removing non-existent node, etc.

    # Test cases for convert_to_dot
    def test_convert_to_dot(self):
        # Test converting graph to DOT format
        original_file_path = "/Users/danyilikonnikov/Desktop/Projects/Sem_2/Miniproject_2/miniproject-2/graph/data1.txt"
        convert_to_dot(original_file_path)
        dot_file_path = original_file_path.split('.')[0] + ".dot"
        self.assertTrue(os.path.exists(dot_file_path))

        # Check if the contents of the DOT file are correct compared to the original file
        graph = get_graph_from_file(original_file_path)
        expected_dot_contents = "digraph {\n"
        for node, edges in to_edge_dict(graph).items():
            for edge in edges:
                expected_dot_contents += f"{node} -> {edge}\n"
        expected_dot_contents += "}"

        with open(dot_file_path, 'r') as dot_file:
            actual_dot_contents = dot_file.read()

        self.assertEqual(actual_dot_contents, expected_dot_contents)

        # Clean up created DOT file after testing
        os.remove(dot_file_path)

if __name__ == '__main__':
    unittest.main()
