from os import pathsep
import numpy as np
class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.max_path = 0
        self.nodes_below = []

    def add_edge(self, to_add):
        self.nodes_below.append(to_add)

    def __str__(self) -> str:
        return str(self.value)
    def __repr__(self):
        return self.__str__()


with open('euler67.txt', 'r') as data:
    valArray = [[int(val) for val in line.strip().split()] for line in data.readlines()]
    head = Node(valArray[0][0])
    last_row_nodes = []
    row_nodes = [head]
    for row in valArray[1:]:
        last_row_nodes = row_nodes
        row_nodes = [Node(val) for val in row]

        i = 0
        for node in last_row_nodes:
            #Append nodes to left
            node.add_edge(row_nodes[i])

            #Append nodes to right
            node.add_edge(row_nodes[i+1])
            i += 1


queue = []
queue.append(head)

max_path = -1

while queue:
    cur_node = queue.pop(0)
    path_sum = cur_node.max_path + cur_node.value

    if len(cur_node.nodes_below) == 0:
        if max_path < path_sum:
            max_path = path_sum
    else: 
        for node in cur_node.nodes_below:
            if path_sum > node.max_path:
                node.max_path = path_sum
                queue.append(node)

print(max_path)