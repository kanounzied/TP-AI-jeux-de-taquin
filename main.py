from board import Board
from node import Node
from tree_search import TreeSearch

if __name__ == '__main__':
    print("============ Jeu De Taquin ============")
    n = input("donner la dimension du Taquin: ")
    board = Board(int(n))
    board.afficher_pieces()
    node = Node(board)
    tree_search = TreeSearch()

    print("** BFS Tree Search **")
    output = tree_search.bfs_search(node)

    # print("** DFS Tree Search **")
    # output2 = tree_search.dfs_search(node)
    #
    # print("** DFS Iterative Tree Search **")
    # output3 = tree_search.dfs_search(node)
