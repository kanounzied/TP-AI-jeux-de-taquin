from board import Board
from node import Node
from tree_search import TreeSearch
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def plot_comparison_results(mahattan_results, miss_placed_pieces_results):
    comp_list = [[mahattan_results[i], miss_placed_pieces_results[i]] for i in range(len(mahattan_results))]
    comp_df = pd.DataFrame(comp_list, columns=['mahattan_heuristic', 'miss_placed_pieces_heuristic'])
    comp_df['number_of_essay'] = comp_df.index

    fig, ax = plt.subplots(figsize=[9, 7])
    ax.plot(comp_df['number_of_essay'], comp_df['mahattan_heuristic'], label="Mahattan Heuristic",
            marker='o', linewidth=2
            )
    ax.plot(comp_df['number_of_essay'], comp_df['miss_placed_pieces_heuristic'], label="Miss Placed Pieces Heuristic",
            marker='o', linewidth=2
            )
    ax.set_xlabel('Number Of Essay')
    ax.set_ylabel('Number of Moves')
    plt.title('Comparison Between Mahattan and Miss Placed Pieces Heuristics')
    plt.legend()
    plt.savefig('./comp.png')
    plt.show()


def execute_and_compare_heuristics():
    SEED_NUMBER = 10
    mahattan_results = []
    miss_placed_pieces_results = []
    for i in range(SEED_NUMBER):
        board = Board(int(n))
        board.afficher_pieces()
        node = Node(board)
        print("** A* search (Mahattan Heuristic) **")
        mahattan_results.append(tree_search.a_etoile(node, tree_search.heuristique_mahattan))
        print("** A* search (Miss Placed Pieces Heuristic) **")
        miss_placed_pieces_results.append(tree_search.a_etoile(node, tree_search.missplaced_pieces_heuristic))

    print(mahattan_results)
    plot_comparison_results(mahattan_results, miss_placed_pieces_results)

if __name__ == '__main__':
    print("============ Jeu De Taquin ============")
    n = ""
    while not n:
        n = input("donner la dimension du Taquin: ")
    board = Board(int(n))
    board.afficher_pieces()
    node = Node(board)
    tree_search = TreeSearch(int(n))

    # k = int(input("donner algo:"))
    # # if k == 1:
    # print("** BFS Tree Search **")
    # output = tree_search.bfs_search(node)
    # # if k == 2:
    # print("** DFS Tree Search **")
    # output2 = tree_search.dfs_search(node)
    # # if k == 3:
    # print("** DFS Iterative Tree Search **")
    # output3 = tree_search.dfs_iterative_search(node)

    print("** A* search **")
    execute_and_compare_heuristics()

    # tree_search.compare_algorithms() # compare all algorithms based on solution paths
