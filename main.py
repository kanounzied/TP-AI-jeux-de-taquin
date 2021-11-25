from board import Board
from node import Node
from tree_search import TreeSearch
import numpy as np


if __name__ == '__main__':
    print("============ Jeu De Taquin ============")
    n = ""
    while not n:
        n = input("donner la dimension du Taquin: ")
    board = Board(int(n))
    board.afficher_pieces()
    node = Node(board)
    tree_search = TreeSearch(int(n))

    k = int(input("donner algo:"))
    if k == 1:
        print("** BFS Tree Search **")
        output = tree_search.bfs_search(node)
    if k==2:
        print("** DFS Tree Search **")
        output2 = tree_search.dfs_search(node)
    if k == 3:
        print("** DFS Iterative Tree Search **")
        output3 = tree_search.dfs_iterative_search(node)

    # print("** A* search **")
    # output4 = tree_search.a_etoile(node)
