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
        # self.used_states[node.board.state.state_matrix_id_gen()] = True
        # self.queue = np.append(self.queue, [node])
        # while not self.queue[0].board.state.isFinal:
        #     print("queue length: ", len(self.queue))  # nodes queue
        #     head = self.queue[0]
        #     print("board: ")
        #     head.board.afficher_pieces()
        #     if self.queue[0].board.state.isFinal:
        #         break
        #     direction_states = self.remove_redondant_nodes(head)
        #     self.queue = np.delete(self.queue, 0)
        #     self.queue = np.append(direction_states, self.queue)
        # self.used_states = {}
        # print("taquin solved: ")
        # self.queue[0].board.afficher_pieces()
        # return self.queue

        print("board: ", node.board.state.isFinal)
        stack = [node]
        self.used_states[node.board.state.state_matrix_id_gen()] = True
        while len(stack) and not node.board.state.isFinal:
            node = stack[-1]
            node.board.afficher_pieces()
            stack.pop()
            if(self.used_states.get(node.board.state.state_matrix_id_gen())) is None:
                self.used_states[node.board.state.state_matrix_id_gen()] = True

            for n in [node.left, node.right, node.up, node.down]:
                if(self.used_states.get(n.board.state.state_matrix_id_gen())) is None:
                    stack.append(n)

        node.board.afficher_pieces()
        if node.board.state.isFinal:
            print("---------------------------------final state is found!")
            return True
        else:
            children = self.remove_redondant_nodes(node)
            found = False
            while not found and len(children) > 0:
                found = self.dfs_search(children.pop(0))
            return found

    def remove_redondant_nodes(self, head: Node):
        nodes = [head.left, head.right, head.up, head.down]
        final_list = []
        for i in nodes:
            if self.used_states.get(i.board.state.state_matrix_id_gen()) is None:
                final_list.append(i)
                self.used_states[i.board.state.state_matrix_id_gen()] = True
        return final_list
