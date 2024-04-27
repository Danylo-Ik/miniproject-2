import unittest
from solution import *

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

if __name__ == "__main__":
    unittest.main()