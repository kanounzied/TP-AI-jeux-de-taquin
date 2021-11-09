from node import Node
import numpy as np


class TreeSearch:
    queue = np.array([])
    used_states = {}

    def bfs_search(self, node: Node):
        self.used_states[node.board.state.state_matrix_id_gen()] = True
        self.queue = np.append(self.queue, [node])
        while not self.queue[0].board.state.isFinal:
            print("queue length: ", len(self.queue))# nodes queue
            head = self.queue[0]
            print("board: ")
            head.board.afficher_pieces()
            if self.queue[0].board.state.isFinal:
                break
            direction_states = self.remove_redondant_nodes(head)
            self.queue = np.append(self.queue, direction_states)
            self.queue = np.delete(self.queue, 0)
        self.used_states = {}
        print("taquin solved: ")
        self.queue[0].board.afficher_pieces()
        return self.queue

    def dfs_search(self, node: Node):
        self.used_states[node.board.state.state_matrix_id_gen()] = True
        self.queue = np.append(self.queue, [node])
        while not self.queue[0].board.state.isFinal:
            print("queue length: ", len(self.queue))  # nodes queue
            head = self.queue[0]
            print("board: ")
            head.board.afficher_pieces()
            if self.queue[0].board.state.isFinal:
                break
            direction_states = self.remove_redondant_nodes(head)
            self.queue = np.delete(self.queue, 0)
            self.queue = np.append(direction_states, self.queue)
        self.used_states = {}
        print("taquin solved: ")
        self.queue[0].board.afficher_pieces()
        return self.queue

    def remove_redondant_nodes(self, head: Node):
        nodes = [head.left, head.right, head.up, head.down]
        final_list = []
        for i in nodes:
            if self.used_states.get(i.board.state.state_matrix_id_gen()) is None:
                final_list.append(i)
                self.used_states[i.board.state.state_matrix_id_gen()] = True
        return final_list
