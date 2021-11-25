from board import Board
from node import Node
from tree_search import TreeSearch
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_comparison_results(mahattan_results, miss_placed_pieces_results):
    comp_list = [[mahattan_results[i], miss_placed_pieces_results[i]] for i in range(len(mahattan_results))]
    print(comp_list)
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

    algo_to_execute = int(input('Enter the number of the algorithm to execute.\n'
                                '1: BFS Search\n'
                                '2: DFS Search\n'
                                '3: Iterative DFS Search\n'
                                '4: A* Search\n'))
    if algo_to_execute == 1:
        print("** BFS Tree Search **")
        output = tree_search.bfs_search(node)
    if algo_to_execute == 2:
        print("** DFS Tree Search **")
        output2 = tree_search.dfs_search(node)
    if algo_to_execute == 3:
        print("** DFS Iterative Tree Search **")
        output3 = tree_search.dfs_iterative_search(node)
    if algo_to_execute == 4:
        execute_and_compare_heuristics()
