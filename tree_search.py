from node import Node
import numpy as np
import math


class TreeSearch:
    open = np.array([])
    closed = {}

    def bfs_search(self, node: Node):
        self.closed[node.board.state.state_matrix_id_gen()] = "root"
        self.open = np.array([
            {
                "parent": "tree",
                "node": node
            }
        ])
        while not self.open[0]["node"].board.state.isFinal:
            print("queue length: ", len(self.open))  # nodes queue
            head = self.open[0]["node"]
            print("board: ")
            head.board.afficher_pieces()
            if head.board.state.isFinal:
                break
            direction_states = self.remove_redondant_nodes(head)
            self.open = np.delete(self.open, 0)
            self.open = np.append(self.open, direction_states)
        print("taquin solved: ")
        # self.open[0]["node"].board.afficher_pieces()
        self.find_solution_path()
        self.closed = {}
        return self.open

    def dfs_search(self, node: Node):

        # ========  5edmet zied

        self.closed[node.board.state.state_matrix_id_gen()] = "root"
        self.open = np.array([
            {
                "parent": "tree",
                "node": node
            }
        ])
        while not self.open[0]["node"].board.state.isFinal:
            print("queue length: ", len(self.open))  # nodes queue
            head = self.open[0]["node"]
            print("board: ")
            head.board.afficher_pieces()
            if head.board.state.isFinal:
                break
            direction_states = self.remove_redondant_nodes(head)
            self.open = np.delete(self.open, 0)
            self.open = np.append(direction_states, self.open)
        print("taquin solved: ")
        self.find_solution_path()
        self.closed = {}
        return self.open

        # ===========  5edmet grati

        # print("board: ", node.board.state.isFinal)
        # stack = [node]
        # self.closed[node.board.state.state_matrix_id_gen()] = True
        # while len(stack) and not node.board.state.isFinal:
        #     node = stack[-1]
        #     node.board.afficher_pieces()
        #     stack.pop()
        #     if (self.closed.get(node.board.state.state_matrix_id_gen())) is None:
        #         self.closed[node.board.state.state_matrix_id_gen()] = True
        #
        #     for n in [node.left, node.right, node.up, node.down]:
        #         if (self.closed.get(n.board.state.state_matrix_id_gen())) is None:
        #             stack.append(n)
        #
        # node.board.afficher_pieces()
        # if node.board.state.isFinal:
        #     print("---------------------------------final state is found!")
        #     self.closed = {}
        #     return True
        # else:
        #     children = self.remove_redondant_nodes(node)
        #     found = False
        #     while not found and len(children) > 0:
        #         found = self.dfs_search(children.pop(0))
        #     if found is True :
        #         self.closed = {}
        #     return found

    def dfs_iterative_search(self, node: Node):
        level = 0
        self.closed[node.board.state.state_matrix_id_gen()] = "root"
        self.open = np.array([{
            "level": level,
            "node": node,
            "parent": "root"
        }])
        index = 0
        while not self.open[index]["node"].board.state.isFinal:
            print("============== level: ", level, " =================")
            index = 0
            children = self.get_leveled_children(self.open[index])
            self.open = np.append(children, self.open)

            while self.open[-1]["node"] != self.open[index]["node"]:  # index != len(self.open)
                self.open[index]["node"].board.afficher_pieces()
                head = self.open[index]
                if head["node"].board.state.isFinal:
                    break
                if head["level"] < level:
                    children = self.get_leveled_children(head)
                    self.open = np.delete(self.open, index)
                    self.open = np.insert(self.open, index, children)
                else:
                    index += 1
            print("break in while!!!!")
            level += 1
        self.find_solution_path(index)
        self.closed = {}
        return self.open

    def remove_redondant_nodes(self, head: Node):
        nodes = [head.left, head.right, head.up, head.down]
        final_list = []
        for node in nodes:
            if self.closed.get(node.board.state.state_matrix_id_gen()) is None:
                final_list.append(
                    {
                        "parent": head.board.state.state_matrix_id_gen(),
                        "node": node
                    }
                )
                self.closed[node.board.state.state_matrix_id_gen()] = head.board.state.state_matrix_id_gen()
        return final_list

    def get_leveled_children(self, head):
        nodes = [head["node"].left, head["node"].right, head["node"].up, head["node"].down]
        final_list = []
        for node in nodes:
            if self.closed.get(node.board.state.state_matrix_id_gen()) is None:
                final_list.append(
                    {
                        "parent": head["node"].board.state.state_matrix_id_gen(),
                        "level": head["level"] + 1,
                        "node": node
                    }
                )
                self.closed[node.board.state.state_matrix_id_gen()] = head["node"].board.state.state_matrix_id_gen()
        return final_list

    def remove_redondant_nodes_safe_copy(self, head: Node):
        nodes = [head.left, head.right, head.up, head.down]
        final_list = []
        for i in nodes:
            if self.closed.get(i.board.state.state_matrix_id_gen()) is None:
                final_list.append(i)
                self.closed[i.board.state.state_matrix_id_gen()] = True
        return final_list

    def find_solution_path(self, index=0):
        parent = self.open[index]["parent"]
        solution_path = np.array([self.open[index]["node"].board.state.state_matrix_id_gen()])
        while parent != "root":
            solution_path = np.append(parent, solution_path)
            parent = self.closed[parent]

        # solution_path = np.append(parent, solution_path)
        print("solution found in ", len(solution_path), " steps!")
        for sol in solution_path:
            self.string_to_matrix(sol)

    def string_to_matrix(self, s):
        size = int(math.sqrt(len(s)))
        matrix = np.empty((size, size), dtype=str)
        for i in range(len(s)):
            if s[i] != '0':
                matrix[i // size][i % size] = s[i]
            else:
                matrix[i // size][i % size] = ' '

        s = [[str(e) for e in row] for row in matrix]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print('--------')
        print('\n'.join(table))
